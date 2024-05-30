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

df_kreuzfahrer['Jahr'] = pd.to_datetime(df_kreuzfahrer['Jahr'], format='%Y')


print (df_kreuzfahrer)


