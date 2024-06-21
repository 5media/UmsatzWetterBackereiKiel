import pandas as pd
from datetime import datetime

# Einlesen der CSV-Dateien
umsatzdaten = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/umsatzdaten_gekuerzt.csv')
passagieraufkommen = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/Passagieraufkommen_neu.csv')

## Bearbeiten der Datei Passagieraufkommen 

# 1. Anzeigen der ersten Zeilen des ursprünglichen Datensatzes
print("Erste Zeilen der Daten:")
print(passagieraufkommen.head())


# Entfernen der unerwünschten Spalten
passagieraufkommen.drop(columns=['pas_faehrverkehr_relativ', 'pas_ausflugsverkehr_relativ', 'pas_kreuzfahrt_relativ'], inplace=True)

# Konvertieren der Jahr-Spalte in ein datetime-Objekt für die Datumserstellung
passagieraufkommen['Jahr'] = pd.to_datetime(passagieraufkommen['Jahr'], format='%Y')

# Liste der Spalten, deren Werte aufgeteilt werden sollen
spalten_zu_teilen = ['Passagiere_ins_abs', 'pas_faehrverkehr_absolut', 'pas_ausflugsverkehr_absolut', 'pas_kreuzfahrt_absolut', 'anzahl_Kreuzfahrtschiff_absolut']

# Erzeugen der täglichen Datensätze
all_data = []
for _, row in passagieraufkommen.iterrows():
    jahr = row['Jahr'].year
    num_days = 366 if pd.Timestamp(year=jahr, month=12, day=31).is_leap_year else 365
    
    for single_date in pd.date_range(start=f'{jahr}-01-01', end=f'{jahr}-12-31'):
        tägliche_werte = {spalte: row[spalte] / num_days for spalte in spalten_zu_teilen}
        tägliche_werte['Datum'] = single_date
        all_data.append(tägliche_werte)

# Erstellen eines neuen DataFrames mit den täglichen Daten
tagesdaten = pd.DataFrame(all_data)

# Löschen der Zeilen ab dem 2019-08-01
datum_zum_loeschen = pd.to_datetime('2019-08-01')
tagesdaten = tagesdaten[tagesdaten['Datum'] < datum_zum_loeschen]

# Anzeigen der ersten Zeilen des neuen DataFrames zur Überprüfung
print("Erste Zeilen der transformierten Daten:")
print(tagesdaten.head())

# Speichern der neuen Daten als CSV-Datei
pfad_zur_ausgabedatei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/Passagieraufkommen_Tagesdaten_bereinigt.csv'
tagesdaten.to_csv(pfad_zur_ausgabedatei, index=False)

print(f"Aktualisierte Daten wurden in '{pfad_zur_ausgabedatei}' gespeichert.")