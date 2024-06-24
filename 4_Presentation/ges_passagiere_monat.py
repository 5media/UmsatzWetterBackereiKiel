import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Daten laden
df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Passagieraufkommen.csv', parse_dates=['Datum'])

# Füge eine Spalte mit dem Jahr und dem Monat hinzu
df['Jahr'] = df['Datum'].dt.year
df['Monat'] = df['Datum'].dt.month

# Aggregiere die Daten nach Jahr und Monat und berechne die Mittelwerte
monthly_means = df.groupby(['Jahr', 'Monat']).agg({
    'pas_faehrverkehr_absolut': 'mean',
    'pas_ausflugsverkehr_absolut': 'mean',
    'pas_kreuzfahrt_absolut': 'mean'
}).reset_index()

# Funktion zur Berechnung des Konfidenzintervalls
def mean_confidence_interval(data, confidence=0.95):
    a = np.array(data.dropna())  # Entferne NaN-Werte vor der Berechnung
    if len(a) <= 1:
        return np.nan, np.nan, np.nan  # Rückgabe von NaN, wenn nicht genügend Datenpunkte vorhanden sind
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

# Berechne Konfidenzintervalle für jeden Monat
def calculate_confidence_intervals(df, monthly_means, column):
    lower_bounds = []
    upper_bounds = []
    for _, row in monthly_means.iterrows():
        subset = df[(df['Jahr'] == row['Jahr']) & (df['Monat'] == row['Monat'])][column]
        mean, lower, upper = mean_confidence_interval(subset)
        lower_bounds.append(lower)
        upper_bounds.append(upper)
    return lower_bounds, upper_bounds

# Berechne die Konfidenzintervalle für jede Passagierart
monthly_means['CI_lower_faehr'], monthly_means['CI_upper_faehr'] = calculate_confidence_intervals(df, monthly_means, 'pas_faehrverkehr_absolut')
monthly_means['CI_lower_ausflug'], monthly_means['CI_upper_ausflug'] = calculate_confidence_intervals(df, monthly_means, 'pas_ausflugsverkehr_absolut')
monthly_means['CI_lower_kreuz'], monthly_means['CI_upper_kreuz'] = calculate_confidence_intervals(df, monthly_means, 'pas_kreuzfahrt_absolut')

# Erstelle das Balkendiagramm für pas_faehrverkehr_absolut
plt.figure(figsize=(15, 8))
plt.bar(monthly_means['Monat'].astype(str) + '-' + monthly_means['Jahr'].astype(str), monthly_means['pas_faehrverkehr_absolut'], 
        yerr=[np.abs(monthly_means['pas_faehrverkehr_absolut'] - monthly_means['CI_lower_faehr']), 
              np.abs(monthly_means['CI_upper_faehr'] - monthly_means['pas_faehrverkehr_absolut'])], 
        capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Monat-Jahr')
plt.ylabel('Durchschnittlich Passagieraufkommen (Fährverkehr)')
plt.title('Durchschnittlich Passagieraufkommen im Fährverkehr pro Monat mit Konfidenzintervallen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Erstelle das Balkendiagramm für pas_ausflugsverkehr_absolut
plt.figure(figsize=(15, 8))
plt.bar(monthly_means['Monat'].astype(str) + '-' + monthly_means['Jahr'].astype(str), monthly_means['pas_ausflugsverkehr_absolut'], 
        yerr=[np.abs(monthly_means['pas_ausflugsverkehr_absolut'] - monthly_means['CI_lower_ausflug']), 
              np.abs(monthly_means['CI_upper_ausflug'] - monthly_means['pas_ausflugsverkehr_absolut'])], 
        capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Monat-Jahr')
plt.ylabel('Durchschnittlich Passagieraufkommen (Ausflugsverkehr)')
plt.title('Durchschnittlich Passagieraufkommen im Ausflugsverkehr pro Monat mit Konfidenzintervallen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Erstelle das Balkendiagramm für pas_kreuzfahrt_absolut
plt.figure(figsize=(15, 8))
plt.bar(monthly_means['Monat'].astype(str) + '-' + monthly_means['Jahr'].astype(str), monthly_means['pas_kreuzfahrt_absolut'], 
        yerr=[np.abs(monthly_means['pas_kreuzfahrt_absolut'] - monthly_means['CI_lower_kreuz']), 
              np.abs(monthly_means['CI_upper_kreuz'] - monthly_means['pas_kreuzfahrt_absolut'])], 
        capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Monat-Jahr')
plt.ylabel('Durchschnittlich Passagieraufkommen (Kreuzfahrt)')
plt.title('Durchschnittlich Passagieraufkommen im Kreuzfahrtverkehr pro Monat mit Konfidenzintervallen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
