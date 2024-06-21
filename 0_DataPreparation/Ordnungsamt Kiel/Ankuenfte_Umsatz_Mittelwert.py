import pandas as pd

# Einlesen der CSV-Dateien
umsatzdaten = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/umsatzdaten_gekuerzt.csv')
ankuenfte = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/Ankuenfte_Monat_neu.csv')


## Bearbeiten der Datei Ankuenfte - Variante Durchschnittswert Ankuenfte pro Tag 

# Anzeigen der ersten Zeilen
print("Erste Zeilen der Daten:")
print(ankuenfte.head())

# 1. Auswahl der relevanten Spalten und Erstellen des Datums
ankuenfte['Datum'] = pd.to_datetime(ankuenfte[['Jahr', 'Monat']].astype(str).apply('-'.join, 1) + '-01')

# 2. Anzahl der Tage im Monat berechnen und Durchschnitt pro Tag berechnen
ankuenfte['days_in_month'] = ankuenfte['Datum'].dt.days_in_month
ankuenfte['avg_Ankuenfte_ins_absolut'] = ankuenfte['Ankuenfte_ins_absolut'] / ankuenfte['days_in_month']
ankuenfte['avg_uebernachtungen_ins_absolut'] = ankuenfte['uebernachtungen_ins_absolut'] / ankuenfte['days_in_month']

# 3. Erstellen eines DataFrame mit täglichen Daten für jeden Tag im Monat
ankuenfte_daily = pd.DataFrame()
for index, row in ankuenfte.iterrows():
    days_in_month = row['days_in_month']
    daily_data = pd.DataFrame({
        'Datum': pd.date_range(start=row['Datum'], periods=days_in_month, freq='D'),
        'avg_Ankuenfte_ins_absolut': row['avg_Ankuenfte_ins_absolut'],
        'avg_uebernachtungen_ins_absolut': row['avg_uebernachtungen_ins_absolut']
    })
    ankuenfte_daily = pd.concat([ankuenfte_daily, daily_data])

# Anzeige des Ergebnisses
print("\nTransformierte Daten:")
print(ankuenfte_daily.head())

# Speichere den aktualisierten DataFrame als CSV-Datei im entsprechenden Ordner
aktualisierte_csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Ankuenfte_daily_Mittelwert.csv'
ankuenfte_daily.to_csv(aktualisierte_csv_datei, index=False)

## Ermitteln des Einflusses der Ankuenfte auf den Umsatz