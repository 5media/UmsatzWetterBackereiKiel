import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Daten laden
df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/sonntage.csv', parse_dates=['Datum'])

# Füge eine Spalte mit dem Jahr hinzu
df['Jahr'] = df['Datum'].dt.year

# Aggregiere die Daten nach Jahr und zähle die Anzahl der Tage pro Jahr
yearly_sales = df.groupby('Jahr').agg({'Verkaufsoffen': ['mean', 'count']}).reset_index()
yearly_sales.columns = ['Jahr', 'Verkaufsoffen', 'Count']

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

# Berechne Konfidenzintervalle für jedes Jahr
yearly_sales['CI_lower'], yearly_sales['CI_upper'] = zip(*yearly_sales.apply(
    lambda row: mean_confidence_interval([row['Verkaufsoffen']] * int(row['Count']))[1:], axis=1))

# Erstelle das Balkendiagramm
plt.figure(figsize=(10, 6))
plt.bar(yearly_sales['Jahr'].astype(str), yearly_sales['Verkaufsoffen'], 
        yerr=[np.abs(yearly_sales['Verkaufsoffen'] - yearly_sales['CI_lower']), 
              np.abs(yearly_sales['CI_upper'] - yearly_sales['Verkaufsoffen'])], 
        capsize=5, color='skyblue', alpha=0.7)

# Diagramm anpassen
plt.xlabel('Jahr')
plt.ylabel('Durchschnittlich Verkaufsoffen')
plt.title('Durchschnittlich Verkaufsoffen pro Jahr mit Konfidenzintervallen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
