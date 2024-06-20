import pandas as pd

# Pfad zur Excel-Datei
Passagieraufkommen = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/Passagieraufkommen_bis-2019_neu.xlsx')

# Lese die Excel-Datei ein
df = pd.read_excel(Passagieraufkommen)

# Speichere DataFrame als CSV-Datei
csv_datei = 'Passagieraufkommen.csv'
df.to_csv(csv_datei, index=False)

# Pfad zur CSV-Datei
Passagieraufkommen_csv = ('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/Passagieraufkommen.csv')

# Lese die CSV-Datei ein
df_Passagieraufkommen = pd.read_csv(Passagieraufkommen_csv)

# Zeige die Spaltenüberschriften an
print(df_Passagieraufkommen.columns)