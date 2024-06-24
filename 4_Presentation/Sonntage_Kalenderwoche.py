import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Daten laden
df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/sonntage.csv', parse_dates=['Datum'])

# Füge eine Spalte mit der Kalenderwoche hinzu
df['Woche'] = df['Datum'].dt.isocalendar().week

# Aggregiere die Daten nach Woche und zähle die Anzahl der Tage pro Woche
weekly_sales = df.groupby('Woche').agg({'Verkaufsoffen': ['mean', 'count']}).reset_index()
weekly_sales.columns = ['Woche', 'Verkaufsoffen', 'Count']

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

# Berechne Konfidenzintervalle für jede Woche
weekly_sales['CI_lower'], weekly_sales['CI_upper'] = zip(*weekly_sales.apply(
    lambda row: mean_confidence_interval([row['Verkaufsoffen']] * int(row['Count']))[1:], axis=1))

# Erstelle das Balkendiagramm
plt.figure(figsize=(10, 6))
plt.bar(weekly_sales['Woche'], weekly_sales['Verkaufsoffen'], 
        yerr=[np.abs(weekly_sales['Verkaufsoffen'] - weekly_sales['CI_lower']), 
              np.abs(weekly_sales['CI_upper'] - weekly_sales['Verkaufsoffen'])], 
        capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Woche')
plt.ylabel('Durchschnittlich Verkaufsoffen')
plt.title('Durchschnittlich Verkaufsoffen pro Woche mit Konfidenzintervallen')
plt.show()
