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

# Selektieren der relevanten Spalten aus den Ankunftsdaten
ankuenfte = ankuenfte[['Jahr', 'Monat', 'Ankuenfte_ins_absolut', 'uebernachtungen_ins_absolut']]

# Berechnen des monatlichen Mittelwerts für Ankuenfte und Übernachtungen
ankuenfte_grouped = ankuenfte.groupby(['Jahr', 'Monat']).mean().reset_index()

# Erstellen einer neuen Spalte 'Datum' mit dem ersten Tag des Monats
ankuenfte_grouped['Datum'] = pd.to_datetime(ankuenfte_grouped[['Jahr', 'Monat']].assign(Ta=1).rename(columns={'Ta': 'day'}))

# Wiederholen der Werte für jeden Tag im Monat
#ankuenfte_daily = ankuenfte_grouped.set_index('Datum').resample('D').ffill().reset_index()

# Anzeigen der umgeformten Daten
# print(ankuenfte_daily.head())

# Konvertieren der 'Datum' Spalte in den Umsatzdaten zu einem Datumsformat
# umsatzdaten['Datum'] = pd.to_datetime(umsatzdaten['Datum'])

# Zusammenführen der Datensätze basierend auf Datum
# merged_data = pd.merge(umsatzdaten, ankuenfte_daily, on='Datum', how='left')

# Unabhängige Variablen (Prädiktoren)
# X = merged_data[['Ankuenfte_ins_absolut', 'uebernachtungen_ins_absolut']]

# Hinzufügen eines konstanten Terms zur unabhängigen Variable (für den Interzept in der Regression)
#X = sm.add_constant(X)
# Abhängige Variable (Ziel)
#y = merged_data['Umsatz']

# Anpassen des linearen Regressionsmodells
#model = sm.OLS(y, X).fit()

# Zusammenfassung des Modells
#print(model.summary())