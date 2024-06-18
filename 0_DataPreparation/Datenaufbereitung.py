import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Einfügen bzw. Laden des Datensatzes
kiel_kreuzfahrer_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/kiel_kreuzfahrer.csv')
kiwo_url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/kiwo.csv"
kiwo_df = pd.read_csv(kiwo_url)
umsaetze_url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/umsatzdaten_gekuerzt.csv"
umsaetze_df = pd.read_csv(umsaetze_url)
wetter_url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/wetter.csv"
wetter_df = pd.read_csv(wetter_url)

# Entfernen der Spalte "Wettercode" aus der csv-Datei bzw. den Daten [Es fehlen Daten, Nutzen des Wettercodes fraglich]
wetter_df = wetter_df.drop(columns=['Wettercode'])


# Bestimmen der gesamten Anzahl an fehlenden Werten
gesamt_fehlende_werte_kiwo = kiwo_df.isnull().sum().sum()
print(f'\nGesamtzahl fehlender Werte KiWo: {gesamt_fehlende_werte_kiwo}')
gesamt_fehlende_werte_kiel_kreuzfahrer = kiel_kreuzfahrer_df.isnull().sum().sum()
print(f'\nGesamtzahl fehlender Werte Kreuzfahrer: {gesamt_fehlende_werte_kiel_kreuzfahrer}')
gesamt_fehlende_werte_umsaetze = umsaetze_df.isnull().sum().sum()
print(f'\nGesamtzahl fehlender Werte Umsaetze: {gesamt_fehlende_werte_umsaetze}')
gesamt_fehlende_werte_wetter = wetter_df.isnull().sum().sum()
print(f'\nGesamtzahl fehlender Werte Wetter: {gesamt_fehlende_werte_wetter}')

# Ergebnis: es gibt fehlende Werte bei den Wetterdaten

# Fehlende Werte pro Spalte ermitteln -  sinnvoll?
fehlende_werte_pro_spalte = wetter_df.isnull().sum()
print('Fehlende Werte pro Spalte:')
print(fehlende_werte_pro_spalte)

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

# Es fehlen 10 konsekutive Werte in der Bewoelkung 
    # Daten außerhalb zur Bewoelkung nur schwer bis gar nicht auffindbar
    # Daher: Median, da eine relativ große Zeitspanne von 10 Tagen fehlt
    # Mittelwert bzw. Nearest Neighbour keine Option

# Ermitteln des Medians aus der Spalte "Bewoelkung"
median_bewoelkung = wetter_df['Bewoelkung'].median()
print(f'Median der Spalte "Bewoelkung": {median_bewoelkung}')

# Fehlende Werte in der Spalte "Bewoelkung" mit dem Median ersetzen
wetter_df['Bewoelkung'].fillna(median_bewoelkung, inplace=True) 
# fillna ersetzt alle fehlenden Werte (NaN) in der Spalte "Bewoelkung" durch den berechneten Median.
# inplace=True stellt sicher, dass die Änderung direkt im ursprünglichen DataFrame erfolgt.

# Testen, ob noch fehlende Werte existieren über das erneute Ausgeben der Gesamtzahl fehlender Werte
gesamt_fehlende_werte_wetter = wetter_df.isnull().sum().sum()
print(f'\nGesamtzahl fehlender Werte Wetter: {gesamt_fehlende_werte_wetter}')
# Ergebnis: Gesamtzahl fehlender Werte ist 0, also alles ok

# Datei als CSV speichern
# wetter_df.to_csv('bereinigtes_wetter.csv', index=False)
