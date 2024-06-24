import pandas as pd

# Daten einlesen
sonntage = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Kiel_verkaufsoffen_sonntag.csv')

# Datum konvertieren
sonntage['Datum'] = pd.to_datetime(sonntage['Datum'])

# Start- und Enddatum definieren
start_date = '2012-06-03'
end_date = '2019-11-03'

# Datenreihe mit allen Daten im Zeitraum erstellen
all_dates = pd.date_range(start=start_date, end=end_date)

# DataFrame mit allen Daten erstellen
all_dates_sonntage = pd.DataFrame(all_dates, columns=['Datum'])

# Löschen aller Zeilen ab Datum '2019-08-01' und vor '2013-04-29'
datum_zum_loeschen = '2019-08-01'
datum_zum_loeschen_2 = '2013-04-29'
all_dates_sonntage = all_dates_sonntage[(all_dates_sonntage['Datum'] < datum_zum_loeschen) & (all_dates_sonntage['Datum'] > datum_zum_loeschen_2)]
print(all_dates_sonntage.head())

# Originaldaten mit vollständigem Datensatz zusammenführen
merged_sonntage = pd.merge(all_dates_sonntage, sonntage, on='Datum', how='left')

# Fehlende Werte in der Spalte 'Verkaufsoffen' mit 0 auffüllen, wobei vorhandene Werte beibehalten werden
merged_sonntage['Verkaufsoffen'] = merged_sonntage['Verkaufsoffen'].fillna(0)

# Die Spalte 'Verkaufsoffen' in Integer umwandeln
merged_sonntage['Verkaufsoffen'] = merged_sonntage['Verkaufsoffen'].astype(int)

# Daten speichern
output_file_path = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/sonntage.csv'
merged_sonntage.to_csv(output_file_path, index=False)

