import pandas as pd
import numpy as np

# Einlesen der CSV-Dateien
pfad_zum_repo_ordner = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/'
umsatzdaten = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/umsatzdaten_gekuerzt.csv')
pfad_zum_repo_ordner = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV'
ankuenfte = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/Ankuenfte_Monat_neu.csv')

# Anzeigen der ersten Zeilen beider Datensätze
umsatzdaten.head(), ankuenfte.head()
print(umsatzdaten.head(), ankuenfte.head())
print("Umsatzdaten:")
print(umsatzdaten.head())
print("\nAnkuenfte:")
print(ankuenfte.head())

# 1. Auswahl der relevanten Spalten
relevant_df_ankuenfte = ankuenfte[['Jahr', 'Monat', 'Ankuenfte_ins_absolut', 'uebernachtungen_ins_absolut']]

# 2. Tagesdatum aus Jahr und Monat erstellen und den monatlichen Durchschnitt berechnen
relevant_df_ankuenfte['Datum'] = pd.to_datetime(relevant_df_ankuenfte[['Jahr', 'Monat',]].astype(str).apply('-'.join, 1) + '-01')

# 3. Berechnung des monatlichen Durchschnitts für jeden Tag im Monat
relevant_df_ankuenfte = relevant_df_ankuenfte.set_index('Datum').resample('D').mean().reset_index()

# Anzeige des Ergebnisses
print("\nTransformierte Daten:")
print(relevant_df_ankuenfte)