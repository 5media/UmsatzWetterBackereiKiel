import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Einfügen bzw. Laden des Datensatzes
wetter_url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/wetter.csv"
wetter_df = pd.read_csv(wetter_url)

# Fehlende Werte pro Spalte ermitteln
fehlende_werte_pro_spalte = wetter_df.isnull().sum()
print('Fehlende Werte pro Spalte:')
print(fehlende_werte_pro_spalte)

# Gesamtzahl fehlender Werte
gesamt_fehlende_werte = wetter_df.isnull().sum().sum()
print(f'\nGesamtzahl fehlender Werte: {gesamt_fehlende_werte}')

# Zeilen mit fehlenden Werten anzeigen
zeilen_mit_fehlenden_werten = wetter_df[wetter_df.isnull().any(axis=1)]
print('\nZeilen mit fehlenden Werten:')
print(zeilen_mit_fehlenden_werten)

# Fehlende Werte spaltenweise ausgeben
print('\nFehlende Werte spaltenweise:')
for column in wetter_df.columns:
    if wetter_df[column].isnull().any():
        fehlende_werte = wetter_df[wetter_df[column].isnull()][column]
        print(f'\nFehlende Werte in Spalte "{column}":')
        print(fehlende_werte)

# Ergebnis: 
    # Es fehlen Werte im Wettercode - da Interpretation notwendig wäre, werden die Wettercodes vorerst rausgenommen:
    # Es fehlen 10 konsekutive Werte in der Bewölkung - Idee: Median oder Quelle außerhalb 

# Entfernen der Spalte "Wettercode" aus der csv-Datei bzw. den Daten
wetter_df = wetter_df.drop(columns=['Wettercode'])

# Ermitteln des Medians aus der Spalte "Bewoelkung"
median_bewoelkung = wetter_df['Bewoelkung'].median()
print(f'Median der Spalte "Bewoelkung": {median_bewoelkung}')

# Fehlende Werte in der Spalte "Bewoelkung" mit dem Median ersetzen
wetter_df['Bewoelkung'].fillna(median_bewoelkung, inplace=True) 
# fillna ersetzt alle fehlenden Werte (NaN) in der Spalte "Bewoelkung" durch den berechneten Median.
# inplace=True stellt sicher, dass die Änderung direkt im ursprünglichen DataFrame erfolgt.

# Testen, ob noch fehlende Werte existieren über das erneute Ausgeben der Gesamtzahl fehlender Werte
gesamt_fehlende_werte = wetter_df.isnull().sum().sum()
print(f'\nGesamtzahl fehlender Werte: {gesamt_fehlende_werte}')
# Ergebnis: Gesamtzahl fehlender Werte ist 0, also alles ok

# Datei als CSV speichern
# wetter_df.to_csv('bereinigtes_wetter.csv', index=False)

# Optional: Fehlende Werte visualisieren
# plt.figure(figsize=(10, 6))
# plt.title('Heatmap der fehlenden Werte im Datensatz')
# sns.heatmap(wetter_df.isnull(), cbar=False, cmap='viridis')
# plt.show()