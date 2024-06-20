import pandas as pd

# Pfad zur Excel-Datei
Passagieraufkommen = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/Passagieraufkommen_bis-2019_neu.xlsx')

# Lese die Excel-Datei ein
df = pd.read_excel(Passagieraufkommen)

# Speichere DataFrame als CSV-Datei
csv_datei = 'Passagieraufkommen.csv'
df.to_csv(csv_datei, index=False)

## Überprüfung der CSV-Datei
# Pfad zur CSV-Datei
Passagieraufkommen_csv = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/Passagieraufkommen.csv')
# Lese die CSV-Datei ein
df_Passagieraufkommen = pd.read_csv(Passagieraufkommen_csv)
# Zeige die Spaltenüberschriften an
print(df_Passagieraufkommen.columns)

# Auffüllen der fehlenden Werte für das Jahr 1989 mit den Werten aus dem Jahr 1990 (Anzahl der Kreuzfahrtschiffe)
columns_to_replace = ['pas_kreuzfahrt_absolut', 'pas_kreuzfahrt_relativ', 'anzahl_Kreuzfahrtschiff_absolut']
df_Passagieraufkommen.loc[0, columns_to_replace] = df.loc[1, columns_to_replace].values

# Zeige den aktualisierten Dataframe an
print(df_Passagieraufkommen.head())

# Speichere den aktualisierten DataFrame als CSV-Datei
aktualisierte_csv_datei = 'Passagieraufkommen_neu.csv'
df_Passagieraufkommen.to_csv(aktualisierte_csv_datei, index=False)