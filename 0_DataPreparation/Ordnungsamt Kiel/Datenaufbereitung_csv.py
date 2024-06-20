import pandas as pd

# Pfad zur Excel-Datei
Passagieraufkommen = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/Passagieraufkommen_bis-2019_neu.xlsx')

# Lese die Excel-Datei ein
df_Passagieraufkommen = pd.read_excel(Passagieraufkommen)

# Speichere DataFrame als CSV-Datei
pfad_zum_repo_ordner = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV' # Pfad zu deinem GitHub-Repository-Ordner
csv_datei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/' + 'Passagieraufkommen.csv'
df_Passagieraufkommen.to_csv(csv_datei, index=False)

## Überprüfung der CSV-Datei
# Pfad zur CSV-Datei
Passagieraufkommen_csv = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/Passagieraufkommen.csv')
# Lese die CSV-Datei ein
df_Passagieraufkommen = pd.read_csv(Passagieraufkommen_csv)
# Zeige die Spaltenüberschriften an
print(df_Passagieraufkommen.columns)

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