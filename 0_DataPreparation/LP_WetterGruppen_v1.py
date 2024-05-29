import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Datamerge
from Datamerge_local import merged_df

# Einlesen der merged-Datei 
df = merged_df

# print (merged_df.head())


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
# print(df_tg.head())

# ------------------------------------------

# Summieren des Umsatzes für jede Temperaturgruppe
umsatz_je_temperaturgruppe = df.groupby('TemperaturGruppe')['Umsatz'].sum()

# Ausgabe der Ergebnisse
# print(umsatz_je_temperaturgruppe)

# ------------------------------------------

# Erstellen des Balkendiagramms
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='TemperaturGruppe', y='Umsatz', estimator=sum, ci=None)

# Anzeigen des Plots
plt.show()

# ------------------------------------------

# Berechnen des maximalen und minimalen Wind
max_wind = df['Windgeschwindigkeit'].max()
min_wind = df['Windgeschwindigkeit'].min()

# Ausgabe der Ergebnisse
print('Maximaler Wind:', max_wind)
print('Minimaler Wind:', min_wind)

# Erstellen der Windgruppen
bins = [5, 10, 15, 20]
labels = ['5-10', '10-15', '15-20']
df['WindGruppe'] = pd.cut(df['Windgeschwindigkeit'], bins=bins, labels=labels, include_lowest=True)

# Ausgabe der ersten Zeilen des DataFrame
# print(df.head())

# ------------------------------------------

# Erstellen des Balkendiagramms
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='WindGruppe', y='Umsatz', estimator=sum, ci=None)

# Anzeigen des Plots
plt.show()

# ------------------------------------------

# Berechnen des maximalen und minimalen Bewölkung
max_bewoelkung = df['Bewoelkung'].max()
min_bewoelkung = df['Bewoelkung'].min()

# Ausgabe der Ergebnisse
print('Maximale Bewoelkung:', max_bewoelkung)
print('Minimale Bewoelkung:', min_bewoelkung)

# Erstelle ein Balkendiagramm
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Bewoelkung', y='Umsatz', estimator=sum, ci=None)

# Anzeigen des Plots
plt.show()


# Erstellen der Bewölkungsgruppen
bins = [-np.inf, 4, 7, np.inf]
labels = ['0-4', '5-7', '8']
df['BewoelkungsGruppe'] = pd.cut(df['Bewoelkung'], bins=bins, labels=labels, include_lowest=True)

# Ausgabe der ersten Zeilen des DataFrame
# print(df.head())

# Summieren des Umsatzes für jede Bewölkungsgruppe
umsatz_je_bewoelkungsgruppe = df.groupby('BewoelkungsGruppe')['Umsatz'].sum()

# Ausgabe der Ergebnisse
#print(umsatz_je_bewoelkungsgruppe)

# Erstellen des Balkendiagramms
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='BewoelkungsGruppe', y='Umsatz', estimator=sum, ci=None)

# Anzeigen des Plots
plt.show()



# ------------------------------------------

# Summieren des Umsatzes für jeden Wettercode
umsatz_je_wettercode = df.groupby('Wettercode')['Umsatz'].sum()

# Ausgabe der Ergebnisse
print(umsatz_je_wettercode)


# Zählen der Daten für jeden Wettercode
daten_je_wettercode = df.groupby('Wettercode').size()

# Ausgabe der Ergebnisse
print(daten_je_wettercode)

# Ermitteln der Gesamtzahl der Daten
gesamtzahl_daten = df.shape[0]

# Ausgabe der Ergebnisse
print('Gesamtzahl der Daten:', gesamtzahl_daten)


# erstellen eines Balkendiagramms
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Wettercode', y='Umsatz', estimator=sum, ci=None)

# Anzeigen des Plots
plt.show()




