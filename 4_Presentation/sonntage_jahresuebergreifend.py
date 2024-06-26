import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import calendar

# Daten laden
df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/sonntage.csv', parse_dates=['Datum'])

# Füge eine Spalte mit dem Monat und dem Jahr hinzu
df['Monat'] = df['Datum'].dt.month
df['Jahr'] = df['Datum'].dt.year

# Gruppiere die Daten nach Monat und Jahr und berechne die Mittelwerte
monthly_means = df.groupby(['Monat', 'Jahr']).agg({
    'Verkaufsoffen': 'mean'
}).reset_index()

# Funktion zur Berechnung des Konfidenzintervalls für einen Monat über alle Jahre
def calculate_confidence_interval(data, confidence=0.95):
    a = np.array(data.dropna())  # Entferne NaN-Werte vor der Berechnung
    if len(a) <= 1:
        return np.nan, np.nan, np.nan  # Rückgabe von NaN, wenn nicht genügend Datenpunkte vorhanden sind
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    lower = np.maximum(0, m - h)  # Setze den unteren Grenzwert auf 0
    upper = m + h
    return m, lower, upper

# Berechne Konfidenzintervalle für jeden Monat über alle Jahre
months = range(1, 13)  # Monate von 1 bis 12
CI_lower = []
CI_upper = []

for month in months:
    subset = monthly_means[monthly_means['Monat'] == month]['Verkaufsoffen']
    
    mean, lower, upper = calculate_confidence_interval(subset)
    
    CI_lower.append(lower)
    CI_upper.append(upper)

# Konvertiere Monatsnummern in Monatsnamen
month_names = [calendar.month_name[m] for m in months]

# Erstelle das Balkendiagramm für die verkaufsoffenen Sonntage
plt.figure(figsize=(15, 8))
plt.bar(month_names, 
        [monthly_means[monthly_means['Monat'] == m]['Verkaufsoffen'].mean() for m in months], 
        yerr=[CI_lower, CI_upper], capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Monat')
plt.ylabel('Durchschnittliche Anzahl an verkaufsoffenen Sonntagen')
plt.title('Variable: verkaufsoffene Sonntage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
