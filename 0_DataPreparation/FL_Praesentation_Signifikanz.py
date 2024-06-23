import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# Daten einlesen
fremdenverkehr_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Fremdenverkehr.csv')
passagieraufkommen_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Passagieraufkommen.csv')
umsaetze_df = pd.read_csv('https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/umsatzdaten_gekuerzt.csv')

# Konvertiere das Datum zu einem datetime-Objekt
fremdenverkehr_df['Datum'] = pd.to_datetime(fremdenverkehr_df['Datum'])
passagieraufkommen_df['Datum'] = pd.to_datetime(passagieraufkommen_df['Datum'])
umsaetze_df['Datum'] = pd.to_datetime(umsaetze_df['Datum'])

# Löschen aller Zeilen ab Datum '2019-08-01' [da außerhalb des Zeitraums]
datum_zum_loeschen = '2019-08-01'
umsaetze_df = umsaetze_df[umsaetze_df['Datum'] < datum_zum_loeschen]

# Daten zusammenführen
df_merged = fremdenverkehr_df.merge(passagieraufkommen_df, on='Datum')
df_merged = df_merged.merge(umsaetze_df, on='Datum')

# Variablen für die Regression definieren
independent_vars = ['pas_kreuzfahrt_absolut', 'uebernachtungen']
X = df_merged[independent_vars]

# Regression für jede Warengruppe durchführen
results = {}
coefficients = []
conf_intervals = []
p_values = []

categories = umsaetze_df.columns[1:]  # Alle Spalten außer 'Datum'

for category in categories:
    y = df_merged[category]
    X_with_constant = sm.add_constant(X)  # fügen Sie eine Konstante für den Interzept hinzu
    model = sm.OLS(y, X_with_constant).fit()
    results[category] = model
    coef = model.params[1:]  # Koeffizienten der unabhängigen Variablen
    conf = model.conf_int().iloc[1:]  # Konfidenzintervalle der unabhängigen Variablen
    p_val = model.pvalues[1:]  # p-Werte der unabhängigen Variablen
    coefficients.append(coef)
    conf_intervals.append(conf)
    p_values.append(p_val)
    print(f'Regressionsergebnisse für {category}:')
    print(model.summary())
    print('\n')

# Erstellen eines DataFrame für die Plot-Daten
coef_df = pd.DataFrame(coefficients, index=categories, columns=independent_vars)
conf_df = pd.DataFrame(conf_intervals, index=categories, columns=pd.MultiIndex.from_product([independent_vars, ['lower', 'upper']]))
p_values_df = pd.DataFrame(p_values, index=categories, columns=independent_vars)

# Plotten der Daten
plt.figure(figsize=(14, 10))

for i, var in enumerate(independent_vars):
    plt.subplot(1, 2, i+1)
    sns.barplot(x=coef_df.index, y=coef_df[var], ci=None)
    plt.errorbar(x=coef_df.index, y=coef_df[var], 
                 yerr=[coef_df[var] - conf_df[(var, 'lower')], conf_df[(var, 'upper')] - coef_df[var]], 
                 fmt='none', c='red', capsize=5)
    plt.title(f'Einfluss von {var} auf den Umsatz je Warengruppe')
    plt.xlabel('Warengruppe')
    plt.xticks(rotation=45)
    plt.ylabel('Koeffizient')

plt.tight_layout()
plt.show()

# Überprüfung der Signifikanz
signifikanzniveau = 0.05
for category in categories:
    print(f'Signifikanzprüfung für {category}:')
    for var in independent_vars:
        p_val = p_values_df.loc[category, var]
        if p_val < signifikanzniveau:
            print(f' - Der Einfluss von {var} auf {category} ist signifikant (p = {p_val:.4f})')
        else:
            print(f' - Der Einfluss von {var} auf {category} ist nicht signifikant (p = {p_val:.4f})')
    print('\n')
