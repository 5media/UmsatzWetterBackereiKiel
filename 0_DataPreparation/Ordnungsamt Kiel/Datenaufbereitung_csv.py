import pandas as pd

# Pfad zur Excel-Datei [alle Dateien]
Passagieraufkommen = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/Passagieraufkommen_bis-2019_neu.xlsx')
Ankuenfte_Monat = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/Ankünfte_Monat_bis-2019_neu.xlsx')
Fremdenverkehr =  ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/Fremdenverkehr_ingesamt_bis-2019_neu.xlsx')
Fremdenverkehr_Variante_2 = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/Fremdenverkehr_ingesamt_bis-2019_Variante_2.xlsx')

# Lese die Excel-Datei ein [alle Dateien]
df_Passagieraufkommen = pd.read_excel(Passagieraufkommen)
df_Ankuenfte_Monat = pd.read_excel(Ankuenfte_Monat)
df_Fremdenverkehr = pd.read_excel(Fremdenverkehr)
df_Fremdenverkehr_Variante_2 = pd.read_excel(Fremdenverkehr_Variante_2)

# Speichere DataFrame als CSV-Datei [alle Dateien]
pfad_zum_repo_ordner = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV' # Pfad zu deinem GitHub-Repository-Ordner
csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Passagieraufkommen.csv'
df_Passagieraufkommen.to_csv(csv_datei, index=False)
csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Ankuenfte_Monat.csv'
df_Ankuenfte_Monat.to_csv(csv_datei, index=False)
csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Fremdenverkehr.csv'
df_Fremdenverkehr.to_csv(csv_datei, index=False)
csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Fremdenverkehr_Variante_2.csv'
df_Fremdenverkehr_Variante_2.to_csv(csv_datei, index=False)

## Ankuenfte_Monat
# Zeige die letzten Zeilen des DataFrames an, um zu sehen, welche Zeilen gelöscht werden sollen
print("Vor dem Löschen:")
print(df_Ankuenfte_Monat.tail())
# Filtern und Löschen der Zeilen mit Jahr 2019 und Monat 8-12 [da die Werte nur bis einschließlich Juli 2019 vorliegen müssen]
df_Ankuenfte_Monat = df_Ankuenfte_Monat[~((df_Ankuenfte_Monat['Jahr'] == 2019) & (df_Ankuenfte_Monat['Monat'] >= 8) & (df_Ankuenfte_Monat['Monat'] <= 12))]
# Zeige die letzten Zeilen des DataFrames an, um sicherzustellen, dass die Zeilen gelöscht wurden
print("Nach dem Löschen:")
print(df_Ankuenfte_Monat.tail(15))
# Speichere den aktualisierten DataFrame als CSV-Datei im entsprechenden Ordner
pfad_zum_repo_ordner = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV' # Pfad zu deinem GitHub-Repository-Ordner
aktualisierte_csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Ankuenfte_Monat_neu.csv'
df_Ankuenfte_Monat.to_csv(aktualisierte_csv_datei, index=False)


## Passagieraufkommen
# Auffüllen der fehlenden Werte für das Jahr 1989 mit den Werten aus dem Jahr 1990 (Anzahl der Kreuzfahrtschiffe)
columns_to_replace = ['pas_kreuzfahrt_absolut', 'pas_kreuzfahrt_relativ', 'anzahl_Kreuzfahrtschiff_absolut']
df_Passagieraufkommen.loc[0, columns_to_replace] = df_Passagieraufkommen.loc[1, columns_to_replace].values
# Zeige den aktualisierten Dataframe an
print(df_Passagieraufkommen.head())
# Ersetze den Wert '1999 1' durch '1999' in der Spalte 'Jahr'
df_Passagieraufkommen['Jahr'] = df_Passagieraufkommen['Jahr'].replace('1999 1', '1999')
# Zeige die aktualisierten Daten an, um sicherzustellen, dass der Wert ersetzt wurde
print(df_Passagieraufkommen)
# Speichere den aktualisierten DataFrame als CSV-Datei im entsprechenden Ordner
pfad_zum_repo_ordner = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV' # Pfad zu deinem GitHub-Repository-Ordner
aktualisierte_csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Passagieraufkommen_neu.csv'
df_Passagieraufkommen.to_csv(aktualisierte_csv_datei, index=False)