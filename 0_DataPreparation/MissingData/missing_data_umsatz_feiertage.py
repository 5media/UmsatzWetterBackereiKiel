import pandas as pd

# Dateien laden
umsatz_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/umsatzdaten_gekuerzt.csv')
feiertage_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/feiertage_sh_ausgeschrieben.csv')
#umsatz_df = pd.read_csv('/workspaces/test/csv/umsatzdaten_gekuerzt.csv')
#feiertage_df = pd.read_csv('/workspaces/test/csv_zusatz/feiertage_sh.csv')

# Datumswerte in datetime-Objekte umwandeln
umsatz_df['Datum'] = pd.to_datetime(umsatz_df['Datum'], format='%Y-%m-%d')
feiertage_df['Datum'] = pd.to_datetime(feiertage_df['Datum'], format='%Y-%m-%d')

# Alle Daten von 2013-07-01 bis 2018-07-31 generieren
all_dates = pd.date_range(start='2013-07-01', end='2018-07-31')

# Fehlende Daten finden
umsatz_dates = umsatz_df['Datum']
missing_dates = all_dates.difference(umsatz_dates)

# Fehlende Daten, die Feiertage sind
feiertage_dates = feiertage_df['Datum']
missing_feiertage = missing_dates.intersection(feiertage_dates)

# Fehlende Daten, die keine Feiertage sind
missing_non_feiertage = missing_dates.difference(feiertage_dates)

# Ergebnisse anzeigen
print(f"Anzahl fehlender Daten: {len(missing_dates)}")
print(f"Anzahl fehlender Daten, die Feiertage sind: {len(missing_feiertage)}")
print(f"Anzahl fehlender Daten, die keine Feiertage sind: {len(missing_non_feiertage)}")

if len(missing_non_feiertage) > 0:
    print("\nFehlende Daten, die keine Feiertage sind:")
    print(missing_non_feiertage)

# Zeilen aus umsatz_df entfernen, die in missing_non_feiertage sind
remaining_entries = umsatz_df[~umsatz_df['Datum'].isin(missing_non_feiertage)]

# Ergebnisse anzeigen
print("\nÜbrige Einträge nach dem Vergleich:")
print(remaining_entries)

# Part 2 Feiertage mit Umsaetzen

# Daten auf den Zeitraum von 2013-07-01 bis 2018-07-31 filtern
umsatz_df = umsatz_df[(umsatz_df['Datum'] >= '2013-07-01') & (umsatz_df['Datum'] <= '2018-07-31')]
feiertage_df = feiertage_df[(feiertage_df['Datum'] >= '2013-07-01') & (feiertage_df['Datum'] <= '2018-07-31')]

# Umsätze an Feiertagen finden
umsatz_feiertage = pd.merge(umsatz_df, feiertage_df, on='Datum', how='inner')

# Ergebnisse anzeigen
print(f"Anzahl der Umsatzeinträge an Feiertagen: {len(umsatz_feiertage)}")
if len(umsatz_feiertage) > 0:
    print("\nUmsatzeinträge an Feiertagen:")
    print(umsatz_feiertage)


# Optional: Ergebnis in eine neue CSV-Datei speichern
#umsatz_feiertage.to_csv('umsatz_an_feiertagen.csv', index=False)

# Part 3 Feiertage ohne Umsaetze

# Feiertage, an denen es Umsätze gab
umsatz_feiertage_dates = umsatz_feiertage['Datum'].unique()

# Feiertage, an denen es keine Umsätze gab
no_umsatz_feiertage = feiertage_df[~feiertage_df['Datum'].isin(umsatz_feiertage_dates)]

# Ergebnisse anzeigen
print(f"Anzahl der Feiertage ohne Umsätze: {len(no_umsatz_feiertage)}")
if len(no_umsatz_feiertage) > 0:
    print("\nFeiertage ohne Umsätze:")
    print(no_umsatz_feiertage)

# Optional: Ergebnis in eine neue CSV-Datei speichern
no_umsatz_feiertage.to_csv('feiertage_ohne_umsatz.csv', index=False)

"""
# Optional: Ergebnis in eine neue CSV-Datei speichern
remaining_entries.to_csv('remaining_umsatzdaten.csv', index=False)
"""
