import pandas as pd
import numpy as np


# Dateine einlesen
umsatz_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/umsatzdaten_gekuerzt.csv')
kiwo_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/kiwo.csv')
wetter_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/wetter.csv')

# Datum zu datetime-Objekten
umsatz_df['Datum'] = pd.to_datetime(umsatz_df['Datum'])
kiwo_df['Datum'] = pd.to_datetime(kiwo_df['Datum'])
wetter_df['Datum'] = pd.to_datetime(wetter_df['Datum'])

# Mergen
merged_df = pd.merge(umsatz_df, kiwo_df, on='Datum', how='left')
merged_df = pd.merge(merged_df, wetter_df, on='Datum', how='left')
