import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Daten einlesen
fremdenverkehr_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Fremdenverkehr.csv')
passagieraufkommen_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Passagieraufkommen.csv')
umsaetze_df = pd.read_csv('https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/umsatzdaten_gekuerzt.csv')

# Konvertiere das Datum zu einem datetime-Objekt
fremdenverkehr_df['Datum'] = pd.to_datetime(fremdenverkehr_df['Datum'])
passagieraufkommen_df['Datum'] = pd.to_datetime(passagieraufkommen_df['Datum'])
umsaetze_df['Datum'] = pd.to_datetime(umsaetze_df['Datum'])

# Löschen aller Zeilen ab Datum '2019-08-01' [da außerhalb des Zeitraums]
datum_zum_loeschen = '2019-08-01'
umsaetze_df = umsaetze_df[umsaetze_df['Datum'] < datum_zum_loeschen]
print(umsaetze_df.head())

# Daten zusammenführen
df_merged = fremdenverkehr_df.merge(passagieraufkommen_df, on='Datum')
df_merged = df_merged.merge(umsaetze_df, on='Datum')

# Funktion zum Berechnen des Konfidenzintervalls
def mean_confidence_interval(data, confidence=0.95):
    n = len(data)
    m, se = data.mean(), stats.sem(data)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

# Berechnung von Mittelwert und Konfidenzintervallen für die Umsätze je Warengruppe
categories = umsaetze_df.columns[1:]  # Alle Spalten außer 'Datum'
means = []
conf_intervals = []

for category in categories:
    m, lower, upper = mean_confidence_interval(df_merged[category])
    means.append(m)
    conf_intervals.append((lower, upper))

# Erstellen eines DataFrame für die Plot-Daten
df_plot = pd.DataFrame({
    'Kategorie': categories,
    'Mittelwert': means,
    'Konfidenzintervall Untergrenze': [ci[0] for ci in conf_intervals],
    'Konfidenzintervall Obergrenze': [ci[1] for ci in conf_intervals]
})

# Plotten der Daten
plt.figure(figsize=(12, 8))
sns.barplot(x='Kategorie', y='Mittelwert', data=df_plot, ci=None)
plt.errorbar(x=df_plot['Kategorie'], y=df_plot['Mittelwert'], 
             yerr=[df_plot['Mittelwert'] - df_plot['Konfidenzintervall Untergrenze'], 
                   df_plot['Konfidenzintervall Obergrenze'] - df_plot['Mittelwert']], 
             fmt='none', c='red', capsize=5)
plt.title('Mittelwert und Konfidenzintervalle der Umsätze je Warengruppe')
plt.xlabel('Warengruppe')
plt.xticks(rotation=45)
plt.ylabel('Mittelwert')
plt.show()

# Beispielhafte Berechnung des Zusammenhangs (Korrelation) zwischen Passagierzahlen und Umsätzen
correlations = df_merged.corr()

# Plot der Korrelationsmatrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm')
plt.title('Korrelationsmatrix zwischen Passagierzahlen und Umsätzen')
plt.show()
