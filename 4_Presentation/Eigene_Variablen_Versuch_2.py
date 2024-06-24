import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Daten einlesen
fremdenverkehr_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Fremdenverkehr.csv')
passagieraufkommen_df = pd.read_csv('/workspaces/UmsatzWetterBackereiKiel/0_DataPreparation/Variablen_CSV/Passagieraufkommen.csv')
umsaetze_df = pd.read_csv('https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/umsatzdaten_gekuerzt.csv')

# Datum konvertieren
umsaetze_df['Datum'] = pd.to_datetime(umsaetze_df['Datum'])
passagieraufkommen_df['Datum'] = pd.to_datetime(passagieraufkommen_df['Datum'])

# Daten zusammenführen
merged_data = pd.merge(umsaetze_df, passagieraufkommen_df, on='Datum')

# Daten in Gruppen unterteilen basierend auf pas_kreuzfahrt_absolut (z.B. Quartile)
merged_data['pas_kreuzfahrt_absolut_group'] = pd.qcut(merged_data['pas_kreuzfahrt_absolut'], q=4, labels=False)

# Durchschnittlichen Umsatz und Konfidenzintervalle pro Warengruppe und Gruppe berechnen
agg_data = merged_data.groupby(['Warengruppe', 'pas_kreuzfahrt_absolut_group']).agg({
    'Umsatz': ['mean', 'sem']
}).reset_index()

agg_data.columns = ['Warengruppe', 'pas_kreuzfahrt_absolut_group', 'mean_Umsatz', 'sem_Umsatz']

# Berechnung der Konfidenzintervalle
agg_data['ci_lower'] = agg_data['mean_Umsatz'] - 1.96 * agg_data['sem_Umsatz']
agg_data['ci_upper'] = agg_data['mean_Umsatz'] + 1.96 * agg_data['sem_Umsatz']

# Balkendiagramm erstellen
plt.figure(figsize=(12, 8))
sns.barplot(x='Warengruppe', y='mean_Umsatz', hue='pas_kreuzfahrt_absolut_group', data=agg_data, capsize=0.1)

# Konfidenzintervalle als Fehlerbalken darstellen
for index, row in agg_data.iterrows():
    plt.errorbar(x=index, y=row['mean_Umsatz'], yerr=row['sem_Umsatz'], fmt='none', c='black', capsize=5)

plt.xlabel('Warengruppe')
plt.ylabel('Durchschnittlicher Umsatz')
plt.title('Einfluss von pas_kreuzfahrt_absolut auf den Umsatz pro Warengruppe')
plt.xticks(rotation=45)
plt.legend(title='pas_kreuzfahrt_absolut Group')
plt.tight_layout()
plt.show()
