import pandas as pd

# Datei laden

#df = pd.read_csv('/workspaces/test/csv/umsatzdaten_gekuerzt.csv')
df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/umsatzdaten_gekuerzt.csv')

# Fehlende Werte pro Spalte anzeigen
missing_values = df.isnull().sum()

print("Anzahl fehlender Werte pro Spalte:")
print(missing_values)

# Gesamtanzahl der fehlenden Werte anzeigen
total_missing = df.isnull().sum().sum()
print("\nGesamtanzahl der fehlenden Werte:")
print(total_missing)

# Beispiel: Anzeigen der ersten 5 Zeilen, um einen Überblick über die Daten zu bekommen
print("\nBeispiel-Daten:")
print(df.head())


#Datumswerte in datetime-Objekte umwandeln
df['Datum'] = pd.to_datetime(df['Datum'], format='%Y-%m-%d')

# Alle Daten von 2012 bis 2019 generieren
all_dates = pd.date_range(start='2013-07-01', end='2018-07-31')

# Fehlende Daten finden
missing_dates = all_dates.difference(df['Datum'])

# Ergebnisse anzeigen
print(f"Anzahl fehlender Daten: {len(missing_dates)}")
if len(missing_dates) > 0:
    print("\nFehlende Daten:")
    print(missing_dates)
else:
    print("\nKeine fehlenden Daten in den Jahren 2013 bis 2019.")
