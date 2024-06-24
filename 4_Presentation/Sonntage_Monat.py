import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Daten laden
df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/sonntage.csv', parse_dates=['Datum'])

# Füge eine Spalte mit dem Monat hinzu
df['Monat'] = df['Datum'].dt.to_period('M')

# Aggregiere die Daten nach Monat und zähle die Anzahl der Tage pro Monat
monthly_sales = df.groupby('Monat').agg({'Verkaufsoffen': ['mean', 'count']}).reset_index()
monthly_sales.columns = ['Monat', 'Verkaufsoffen', 'Count']

# Funktion zur Berechnung des Konfidenzintervalls
def mean_confidence_interval(data, confidence=0.95):
    if len(data) < 2:
        return data[0], data[0], data[0]
    else:
        a = np.array(data)
        n = len(a)
        m, se = np.mean(a), stats.sem(a)
        h = se * stats.t.ppf((1 + confidence) / 2., n-1)
        return m, m-h, m+h

# Berechne Konfidenzintervalle für jeden Monat
monthly_sales['CI_lower'], monthly_sales['CI_upper'] = zip(*monthly_sales.apply(
    lambda row: mean_confidence_interval([row['Verkaufsoffen']] * int(row['Count']))[1:], axis=1))

# Erstelle das Balkendiagramm
plt.figure(figsize=(12, 6))
plt.bar(monthly_sales['Monat'].astype(str), monthly_sales['Verkaufsoffen'], 
        yerr=[np.abs(monthly_sales['Verkaufsoffen'] - monthly_sales['CI_lower']), 
              np.abs(monthly_sales['CI_upper'] - monthly_sales['Verkaufsoffen'])], 
        capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Monat')
plt.ylabel('Durchschnittlich Verkaufsoffen')
plt.title('Durchschnittlich Verkaufsoffen pro Monat mit Konfidenzintervallen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
