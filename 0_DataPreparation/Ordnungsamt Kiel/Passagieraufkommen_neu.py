import pandas as pd
from datetime import datetime

# Einlesen der CSV-Dateien
umsatzdaten = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/umsatzdaten_gekuerzt.csv')
passagieraufkommen = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/Passagieraufkommen_neu.csv')

## Bearbeiten der Datei Passagieraufkommen 

# 1. Anzeigen der ersten Zeilen des ursprünglichen Datensatzes
print("Erste Zeilen der Daten:")
print(passagieraufkommen.head())

# 2. Entfernen der unerwünschten Spalten
passagieraufkommen = passagieraufkommen.drop(columns=['pas_faehrverkehr_relativ', 'pas_ausflugsverkehr_relativ', 'pas_kreuzfahrt_relativ'])

# Konvertieren der Jahr-Spalte in ein datetime-Objekt für die Datumserstellung
# passagieraufkommen['Jahr'] = pd.to_datetime(passagieraufkommen['Jahr'], format='%Y')

# 3. Liste der Spalten, deren Werte aufgeteilt werden sollen
spalten_zu_teilen = ['Passagiere_ins_abs', 'pas_faehrverkehr_absolut', 'pas_ausflugsverkehr_absolut', 'pas_kreuzfahrt_absolut', 'anzahl_Kreuzfahrtschiff_absolut']

# 4. Erzeugen der täglichen Datensätze
all_data = []
for _, row in passagieraufkommen.iterrows():
    jahr = row['Jahr']
    num_days = 366 if datetime(jahr, 12, 31).strftime('%j') == '366' else 365
    
    for single_date in pd.date_range(start=f'{jahr}-01-01', end=f'{jahr}-12-31'):
        tägliche_werte = {spalte: row[spalte] / num_days for spalte in spalten_zu_teilen}
        tägliche_werte['Datum'] = single_date
        all_data.append(tägliche_werte)

# 5. Erstellen eines neuen DataFrames mit den täglichen Daten
passagieraufkommen_daily = pd.DataFrame(all_data)

# 6. Anzeigen der ersten Zeilen des neuen DataFrames zur Überprüfung
print("Erste Zeilen der transformierten Daten:")
print(passagieraufkommen_daily.head())

# 6. Löschen aller Zeilen ab Datum '2019-08-01' [da außerhalb des Zeitraums]
datum_zum_loeschen = '2019-08-01'
passagieraufkommen_daily = passagieraufkommen_daily[passagieraufkommen_daily['Datum'] < datum_zum_loeschen]

# Speichere den aktualisierten DataFrame als CSV-Datei im entsprechenden Ordner
aktualisierte_csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Passagieraufkommen_daily.csv'
passagieraufkommen_daily.to_csv(aktualisierte_csv_datei, index=False)
