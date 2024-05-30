import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Datamerge
from Datamerge_local import merged_df

# Einlesen der merged-Datei 
df = merged_df

# -------------------------------------------------------------------------

# Berechnen des Umsatzes je Warengruppe
umsatz_je_warengruppe = df.groupby('Warengruppe')['Umsatz'].sum()


# Ausgabe des Ergebnisses
print(umsatz_je_warengruppe)

#  Balkendiagramm erstellen
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Warengruppe', y='Umsatz', estimator=sum, ci=None)

# Anzeigen des Plots
plt.show()

# -------------------------------------------------------------------------

# Berechnen der durchschnittlichen Temperatur je Warengruppe
# durchschnittliche_temperatur = df.groupby('Warengruppe')['Temperatur'].mean()

# Ausgabe des Ergebnisses
# print(durchschnittliche_temperatur)



import statsmodels.formula.api as smf

# Fit the linear model
mod = smf.ols('Umsatz ~ Temperatur + C(Warengruppe)', data=merged_df).fit()
# Print the summary
print(mod.summary())

# -------------------------------------------------------------------------

# Erstellen des Scatterplots und der Regressionslinie für jede Warengruppe
for warengruppe in merged_df['Warengruppe'].unique():
    data = merged_df[merged_df['Warengruppe'] == warengruppe]
    plt.scatter(data['Temperatur'], data['Umsatz'], label=warengruppe)
    # Vorhersagen des Modells für die aktuelle Warengruppe
    data['Vorhersage'] = mod.predict(data)
    plt.plot(data['Temperatur'], data['Vorhersage'], color='red')

plt.xlabel('Temperatur')
plt.ylabel('Umsatz')
plt.legend()
plt.show()


