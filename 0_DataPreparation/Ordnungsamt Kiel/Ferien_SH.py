import pandas as pd

# Daten einlesen
ferien_xlsx = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/Ferien_SH.xlsx')
df_ferien = pd.read_excel(ferien_xlsx)

# Speichere DataFrame als CSV-Datei [alle Dateien]
pfad_zum_repo_ordner = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV' 
csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'ferien.csv'
df_ferien.to_csv(csv_datei, index=False)

# CSV einlesen
ferien = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/ferien.csv')

# Definiere den Zeitraum von 2013-04-30 bis 2019-07-31
start_date = '2013-04-30'
end_date = '2019-07-31'

# Erstelle ein DataFrame mit allen Tagen im Zeitraum
date_range = pd.date_range(start=start_date, end=end_date)
df_complete = pd.DataFrame(date_range, columns=['Datum'])

# Lade die vorhandenen Feriendaten aus der CSV-Datei
df_ferien = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/ferien.csv', parse_dates=['Datum'])

# Setze den Index auf 'Datum', falls er noch nicht gesetzt ist
if 'Datum' not in df_ferien.columns:
    df_ferien.set_index('Datum', inplace=True)

# Füge die Spalte 'Ferien' basierend auf vorhandenen Daten hinzu
df_complete = df_complete.merge(df_ferien, on='Datum', how='left')

# Ersetze NaN-Werte in der Spalte 'Ferien' mit 0 (nur für neu hinzugefügte Zeilen)
df_complete['Ferien'].fillna(0, inplace=True)

# Speichere das aktualisierte DataFrame als CSV-Datei
output_csv ='/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/schulferien.csv'
df_complete.to_csv(output_csv, index=False)