import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Datamerge
from Datamerge_local import merged_df

# Einlesen der merged-Datei 
df = merged_df

# -------------------------------------------------------------------------

sns.scatterplot(x='Temperatur', y='Umsatz', data=df, hue='Warengruppe')


xs = df['Temperatur'] .to_numpy().reshape(-1, 1)
ys = df['Umsatz'].to_numpy()


print ('Temperatur')
print(xs.shape)

print ('Umsatz')
print(ys.shape)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xs, ys)

print ('Coef - Intercept')
print(model.coef_, model.intercept_)

# Predict
def get_umsatz(temperatur):
    return model.coef_ * temperatur + model.intercept_

print ('Predict Umsatz 30 Grad Celsius')
print(get_umsatz(30))



