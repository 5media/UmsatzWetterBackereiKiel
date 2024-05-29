import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Datamerge
from Datamerge_local import merged_df

# Einlesen der merged-Datei 
df = merged_df

# -------------------------------------------------------------------------

print ('Scatterplot Temperatur Umsatz Warengruppen')
sns.scatterplot(x='Temperatur', y='Umsatz', data=df, hue='Warengruppe', palette='bright')


plt.show()



xs = df['Temperatur'] .to_numpy().reshape(-1, 1)
ys = df['Umsatz'].to_numpy()


print ('Temperatur')
print(xs.shape)
print ('\n')

print ('Umsatz')
print(ys.shape)
print ('\n')


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xs, ys)

print ('Coef - Intercept')
print(model.coef_, model.intercept_)
print ('\n')

# Predict
def get_umsatz(temperatur):
    return model.coef_ * temperatur + model.intercept_



print ('Predict Umsatz 30 Grad Celsius')
print(get_umsatz(30))
print ('\n')
# -------------------------------------------------------------------------



# Erstellen des OLS Modells
ols_model = LinearRegression()

# Anpassen des Modells an die Daten
ols_model.fit(xs, ys)

# Ausgabe der Koeffizienten und des Achsenabschnitts
print('Koeffizienten:', ols_model.coef_)
print('Achsenabschnitt:', ols_model.intercept_)
print ('\n')

print ('Scatterplot Linear Regression')
# Erstellen des Scatterplots
plt.scatter(xs, ys, color='blue')
plt.plot(xs, ols_model.predict(xs), color='red')
plt.xlabel('Temperatur')
plt.ylabel('Umsatz')
plt.show()
