import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Datamerge
from Datamerge_local import merged_df

# Einlesen der merged-Datei 
df = merged_df

# print (merged_df.head())

# Einlesen Kreuzfahrerdaten
df_kreuzfahrer = pd.read_csv('kiel_passagiere_kreuzfahrten.csv')

# print (df_kreuzfahrer.head())

