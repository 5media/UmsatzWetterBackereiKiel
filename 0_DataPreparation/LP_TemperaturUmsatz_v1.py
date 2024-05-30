import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Datamerge
from Datamerge_local import merged_df

# Einlesen der merged-Datei 
df = merged_df

# ------------------------------------------

# Berechnen des maximalen und minimalen Temperaturwerts
max_temperatur = df['Temperatur'].max()
min_temperatur = df['Temperatur'].min()

# Ausgabe der Ergebnisse
print('Maximale Temperatur:', max_temperatur)
print('Minimale Temperatur:', min_temperatur)

# ------------------------------------------

# Erstellen der Temperaturgruppen
bins = [10, 15, 20, 25, 30]
labels = ['10-15', '15-20', '20-25', '25-30']
df_tg=df['TemperaturGruppe'] = pd.cut(df['Temperatur'], bins=bins, labels=labels, include_lowest=True)

# Ausgabe der ersten Zeilen des DataFrame
print(df_tg.head())

print(df.head())

# ------------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt

# Erstellen des Scatterplots
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='TemperaturGruppe', y='Umsatz')

# Anzeigen des Plots
plt.show()

# ------------------------------------------

# Summieren des Umsatzes für jede Temperaturgruppe
umsatz_je_temperaturgruppe = df.groupby('TemperaturGruppe')['Umsatz'].sum()

# Ausgabe der Ergebnisse
print(umsatz_je_temperaturgruppe)

# ------------------------------------------

# Erstellen des Balkendiagramms
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='TemperaturGruppe', y='Umsatz', estimator=sum, ci=None)

# Anzeigen des Plots
plt.show()