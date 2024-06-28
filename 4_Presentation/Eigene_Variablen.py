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

# Warengruppen aggregieren und Konfidenzintervalle berechnen
agg_data = merged_data.groupby('Warengruppe').agg({
    'Umsatz': ['mean', 'sem']
}).reset_index()

agg_data.columns = ['Warengruppe', 'mean_Umsatz', 'sem_Umsatz']

# Berechnung der Konfidenzintervalle
agg_data['ci_lower'] = agg_data['mean_Umsatz'] - 1.96 * agg_data['sem_Umsatz']
agg_data['ci_upper'] = agg_data['mean_Umsatz'] + 1.96 * agg_data['sem_Umsatz']

# Berechnung der yerr-Werte (Differenz zwischen Mittelwert und Konfidenzintervall)
agg_data['yerr'] = 1.96 * agg_data['sem_Umsatz']

# Balkendiagramm erstellen
plt.figure(figsize=(10, 6))
sns.barplot(x='Warengruppe', y='mean_Umsatz', data=agg_data, capsize=0.1)

# Konfidenzintervalle als Fehlerbalken darstellen
for index, row in agg_data.iterrows():
    plt.errorbar(x=index, y=row['mean_Umsatz'], yerr=row['yerr'], fmt='none', c='black', capsize=5)

plt.xlabel('Warengruppe')
plt.ylabel('Durchschnittlicher Umsatz')
plt.title('Durchschnittlicher Umsatz je Warengruppe mit Konfidenzintervallen')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Grafik speichern
#plt.savefig(f'Durchschnittlicher_Umsatz_Warengruppe.png')