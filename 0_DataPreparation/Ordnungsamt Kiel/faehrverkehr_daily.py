
import pandas as pd
from datetime import datetime

# Einlesen der CSV-Dateien
umsatzdaten = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/umsatzdaten_gekuerzt.csv')
#umsatzdaten = pd.read_csv('csv/umsatzdaten_gekuerzt.csv')
#faehrverkehr = pd.read_csv('csv_zusatz/Faehrverkehr_2012-2019.csv')
faehrverkehr = pd.read_csv('//workspaces/UmsatzWetterBackereiKiel/0_DataPreparation//Ordnungsamt Kiel/CSV/Faehrverkehr_2012-2019.csv')
## Bearbeiten der Datei Faehrverkehr 



# 1. Anzeigen der ersten Zeilen des ursprünglichen Datensatzes
print("Erste Zeilen der Daten:")
print(faehrverkehr.head())

"""
# 1.1  Anzeigen der ersten Zeilen des ursprünglichen Datensatzes
print("Erste Zeilen der Daten 1.1:")
print(umsatzdaten.head())
"""

# Datentypen der Spalten anzeigen
print("Datentypen der Spalten:")
faehrverkehr.info()


# 2. Entfernen der unerwünschten Spalten
# drop(columns=[''])

#Konvertieren der Jahr-Spalte in ein datetime-Objekt für die Datumserstellung
#faehrverkehr['Jahr'] = pd.to_datetime(faehrverkehr['Jahr'], format='%Y')
#faehrverkehr.info()


# 3. Liste der Spalten, deren Werte aufgeteilt werden sollen
spalten_zu_teilen = ['Passagiere_Ein', 'Passagiere_Aus', 'Passagiere_gesamt', 'Passagier-PKW_Ein', 'Passagier-PKW_Aus', 'Passagier-PKW_gesamt', 'PKW-Anhaenger_Ein', 'PKW-Anhaenger_Aus', 'PKW-Anhaenger_gesamt','Omnibusse_Ein', 'Omnibusse_Aus', 'Omnibusse_gesamt','Motorraeder_Ein', 'Motorraeder_Aus', 'Motorraeder_gesamt']

# 4. Erzeugen der täglichen Datensätze
all_data = []
for _, row in faehrverkehr.iterrows():
    jahr = row['Jahr']
    num_days = 366 if datetime(jahr, 12, 31).strftime('%j') == '366' else 365
    
    for single_date in pd.date_range(start=f'{jahr}-01-01', end=f'{jahr}-12-31'):
        
        tägliche_werte = {spalte: row[spalte] / num_days for spalte in spalten_zu_teilen}
        tägliche_werte['Datum'] = single_date
        all_data.append(tägliche_werte)

# 5. Erstellen eines neuen DataFrames mit den täglichen Daten
faehrverkehr_daily = pd.DataFrame(all_data)

# 6. Anzeigen der ersten Zeilen des neuen DataFrames zur Überprüfung
print("Erste Zeilen der transformierten Daten:")
print(faehrverkehr_daily.head())

# 6. Löschen aller Zeilen ab Datum '2019-08-01' [da außerhalb des Zeitraums]
datum_zum_loeschen = '2019-08-01'
faehrverkehr_daily = faehrverkehr_daily[faehrverkehr_daily['Datum'] < datum_zum_loeschen]
datum_zum_loeschen_2 = '2013-04-29'
faehrverkehr_daily = faehrverkehr_daily[faehrverkehr_daily['Datum'] > datum_zum_loeschen_2]

# Letzte Spalte bestimmen
last_column = faehrverkehr_daily.columns[-1]

# Letzte Spalte entfernen und an die erste Position einfügen
faehrverkehr_daily.insert(0, last_column, faehrverkehr_daily.pop(last_column))


# 6. Anzeigen der ersten Zeilen des neuen DataFrames zur Überprüfung
print("Erste Zeilen der transformierten Daten:")
print(faehrverkehr_daily.head())



# Speichere den aktualisierten DataFrame als CSV-Datei im entsprechenden Ordner
aktualisierte_csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Faehrverkehr_2012-2019_daily.csv'
#aktualisierte_csv_datei = '/workspaces/test/csv_zusatz/' + 'Faehrverkehr_2012-2019_daily.csv'
faehrverkehr_daily.to_csv(aktualisierte_csv_datei, index=False)


