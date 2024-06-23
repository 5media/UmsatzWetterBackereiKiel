import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


fremdenverkehr = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Fremdenverkehr.csv'
passagieraufkommen = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Passagieraufkommen.csv'
umsaetze_url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/umsatzdaten_gekuerzt.csv"
umsaetze_df = pd.read_csv(umsaetze_url)

# Löschen aller Zeilen ab Datum '2019-08-01' [da außerhalb des Zeitraums]
datum_zum_loeschen = '2013-04-29'
umsaetze_df = umsaetze_df[umsaetze_df['Datum'] > datum_zum_loeschen]
print(umsaetze_df.head())

# 7. Speichern des aktualisierten DataFrame als CSV-Datei im entsprechenden Ordner
pfad_zur_ausgabedatei = '/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Ordnungsamt Kiel/CSV/umsatz_praesentation.csv'
umsaetze_df.to_csv(pfad_zur_ausgabedatei, index=False)
