import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Import Datamerge
from Datamerge import merged_df

# Einlesen der merged-Datei 
df = merged_df

# Berechnen des Umsatzes je Warengruppe
umsatz_je_warengruppe = df.groupby('Warengruppe')['Umsatz'].sum()

# Ausgabe des Ergebnisses
print(umsatz_je_warengruppe)


# Berechnen des durchschnittlichen Umsatzes je Temperatur und Warengruppe
durchschnittlicher_umsatz = df.groupby(['Temperatur', 'Warengruppe'])['Umsatz'].mean().reset_index()

# Erstellen des Diagramms
for warengruppe in durchschnittlicher_umsatz['Warengruppe'].unique():
    data = durchschnittlicher_umsatz[durchschnittlicher_umsatz['Warengruppe'] == warengruppe]
    plt.plot(data['Temperatur'], data['Umsatz'], label=warengruppe)

plt.xlabel('Temperatur')
plt.ylabel('Durchschnittlicher Umsatz')
plt.legend()
plt.show()



import statsmodels.formula.api as smf

# Fit the linear model
mod = smf.ols('Umsatz ~ Temperatur + C(Warengruppe)', data=merged_df).fit()
# Print the summary
print(mod.summary())