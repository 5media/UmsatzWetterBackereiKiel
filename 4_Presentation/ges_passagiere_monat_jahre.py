import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import calendar  # Importiere das calendar Modul für Monatsnamen

# Daten laden
df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Passagieraufkommen.csv', parse_dates=['Datum'])

# Füge eine Spalte mit dem Jahr und dem Monat hinzu
df['Jahr'] = df['Datum'].dt.year
df['Monat'] = df['Datum'].dt.month

# Gruppiere die Daten nach Jahr und Monat und berechne die Mittelwerte
monthly_means = df.groupby(['Monat', 'Jahr']).agg({
    'pas_faehrverkehr_absolut': 'mean',
    'pas_ausflugsverkehr_absolut': 'mean',
    'pas_kreuzfahrt_absolut': 'mean'
}).reset_index()

# Funktion zur Berechnung des Konfidenzintervalls für einen Monat über alle Jahre
def calculate_confidence_interval(data, confidence=0.95):
    a = np.array(data.dropna())  # Entferne NaN-Werte vor der Berechnung
    if len(a) <= 1:
        return np.nan, np.nan, np.nan  # Rückgabe von NaN, wenn nicht genügend Datenpunkte vorhanden sind
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

# Berechne Konfidenzintervalle für jeden Monat über alle Jahre
months = range(1, 13)  # Monate von 1 bis 12
CI_lower_faehr = []
CI_upper_faehr = []
CI_lower_ausflug = []
CI_upper_ausflug = []
CI_lower_kreuz = []
CI_upper_kreuz = []

for month in months:
    subset_faehr = monthly_means[monthly_means['Monat'] == month]['pas_faehrverkehr_absolut']
    subset_ausflug = monthly_means[monthly_means['Monat'] == month]['pas_ausflugsverkehr_absolut']
    subset_kreuz = monthly_means[monthly_means['Monat'] == month]['pas_kreuzfahrt_absolut']
    
    mean_faehr, lower_faehr, upper_faehr = calculate_confidence_interval(subset_faehr)
    mean_ausflug, lower_ausflug, upper_ausflug = calculate_confidence_interval(subset_ausflug)
    mean_kreuz, lower_kreuz, upper_kreuz = calculate_confidence_interval(subset_kreuz)
    
    CI_lower_faehr.append(lower_faehr)
    CI_upper_faehr.append(upper_faehr)
    CI_lower_ausflug.append(lower_ausflug)
    CI_upper_ausflug.append(upper_ausflug)
    CI_lower_kreuz.append(lower_kreuz)
    CI_upper_kreuz.append(upper_kreuz)

# Konvertiere Monatsnummern in Monatsnamen
month_names = [calendar.month_name[m] for m in months]

# Erstelle das Balkendiagramm für das Passagieraufkommen im Fährverkehr
plt.figure(figsize=(15, 8))
plt.bar(month_names, 
        [monthly_means[monthly_means['Monat'] == m]['pas_faehrverkehr_absolut'].mean() for m in months], 
        yerr=[CI_lower_faehr, CI_upper_faehr], capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Monat')
plt.ylabel('Durchschnittlich Passagieraufkommen (Fährverkehr)')
plt.title('Durchschnittlich Passagieraufkommen im Fährverkehr pro Monat mit Konfidenzintervallen über alle Jahre')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Erstelle das Balkendiagramm für das Passagieraufkommen im Ausflugsverkehr
plt.figure(figsize=(15, 8))
plt.bar(month_names, 
        [monthly_means[monthly_means['Monat'] == m]['pas_ausflugsverkehr_absolut'].mean() for m in months], 
        yerr=[CI_lower_ausflug, CI_upper_ausflug], capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Monat')
plt.ylabel('Durchschnittlich Passagieraufkommen (Ausflugsverkehr)')
plt.title('Durchschnittlich Passagieraufkommen im Ausflugsverkehr pro Monat mit Konfidenzintervallen über alle Jahre')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Erstelle das Balkendiagramm für das Passagieraufkommen im Kreuzfahrtverkehr
plt.figure(figsize=(15, 8))
plt.bar(month_names, 
        [monthly_means[monthly_means['Monat'] == m]['pas_kreuzfahrt_absolut'].mean() for m in months], 
        yerr=[CI_lower_kreuz, CI_upper_kreuz], capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Monat')
plt.ylabel('Durchschnittlich Passagieraufkommen (Kreuzfahrt)')
plt.title('Durchschnittlich Passagieraufkommen im Kreuzfahrtverkehr pro Monat mit Konfidenzintervallen über alle Jahre')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
