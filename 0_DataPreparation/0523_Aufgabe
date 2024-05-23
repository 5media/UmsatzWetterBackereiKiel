import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# Dateine einlesen
umsatz_df = pd.read_csv('/workspaces/test_repo/0_DataPreparation/umsatzdaten_gekuerzt.csv')
kiwo_df = pd.read_csv('/workspaces/test_repo/0_DataPreparation/kiwo.csv')
wetter_df = pd.read_csv('/workspaces/test_repo/0_DataPreparation/wetter.csv')

# Datum zu datetime-Objekten
umsatz_df['Datum'] = pd.to_datetime(umsatz_df['Datum'])
kiwo_df['Datum'] = pd.to_datetime(kiwo_df['Datum'])
wetter_df['Datum'] = pd.to_datetime(wetter_df['Datum'])

# Mergen
merged_df = pd.merge(umsatz_df, kiwo_df, on='Datum', how='inner')
merged_df = pd.merge(merged_df, wetter_df, on='Datum', how='inner')

# Wochentag als kategorielle Variable
merged_df['Wochentag'] = merged_df['Datum'].dt.dayofweek

# Lineare Regression
model_formula = 'Umsatz ~ Temperatur + C(Wochentag)' # Umsatz in Abhängigkeit von Temperatur und Wochentagen
model = smf.ols(model_formula, data=merged_df).fit()

# Modellzusammenfassung
print(model.summary())