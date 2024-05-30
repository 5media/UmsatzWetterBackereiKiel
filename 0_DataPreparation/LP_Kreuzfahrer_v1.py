import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Datamerge
from Datamerge_local import merged_df

# Einlesen der merged-Datei 
df = merged_df


# Einlesen Kreuzfahrerdaten
df_kreuzfahrer = pd.read_csv('kiel_kreuzfahrer.csv')

print (df_kreuzfahrer.head())

# df_kreuzfahrer['Jahr'] = pd.to_datetime(df_kreuzfahrer['Jahr'], format='%Y')
# print (df_kreuzfahrer)


# Stellen Sie sicher, dass 'Datum' im datetime Format ist
df['Datum'] = pd.to_datetime(df['Datum'])

# Erstellen Sie eine neue Spalte 'Jahr', die das Jahr aus 'Datum' extrahiert
df['Jahr'] = df['Datum'].dt.year

print (df.head())

# merge df_kreuzfahrer with df
df = pd.merge(df, df_kreuzfahrer, on='Jahr', how='inner')

print (df.head())

import matplotlib.pyplot as plt

# Gruppieren Sie das DataFrame nach 'Jahr' und summieren Sie 'Umsatz' und 'Kreuzfahrer'
# df_sum = df.groupby('Jahr')[['Umsatz', 'Kreuzfahrer']].sum().reset_index()





