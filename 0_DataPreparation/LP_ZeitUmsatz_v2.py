import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Datamerge
from Datamerge_local import merged_df
# Einlesen der merged-Datei 
df = merged_df

# Stellen Sie sicher, dass 'Datum' im datetime Format ist
df['Datum'] = pd.to_datetime(df['Datum'])

# Extrahieren Sie den Monat und das Jahr aus 'Datum'
df['Monat'] = df['Datum'].dt.month
df['Jahr'] = df['Datum'].dt.year

# Gruppieren Sie das DataFrame nach 'Monat' und 'Jahr' und summieren Sie 'Umsatz'
df_sum = df.groupby(['Jahr', 'Monat'])['Umsatz'].sum().reset_index()

# print(df_sum.head(50))

# Erstellen Sie ein neues DataFrame, das nur die Daten für das Jahr 2013 enthält
df_2013 = df_sum[df_sum['Jahr'] == 2013]
print(df_2013.head())

# Erstellen Sie ein neues DataFrame, das nur die Daten für das Jahr 2014 enthält
df_2014 = df_sum[df_sum['Jahr'] == 2014]
print(df_2014.head())

# Erstellen Sie ein neues DataFrame, das nur die Daten für das Jahr 2015 enthält
df_2015 = df_sum[df_sum['Jahr'] == 2015]
print(df_2015.head())


# Erstellen Sie ein neues DataFrame, das nur die Daten für das Jahr 2016 enthält
df_2016 = df_sum[df_sum['Jahr'] == 2016]
print(df_2016.head())

# Erstellen Sie ein neues DataFrame, das nur die Daten für das Jahr 2017 enthält
df_2017 = df_sum[df_sum['Jahr'] == 2017]
print(df_2017.head())

# Erstellen Sie ein neues DataFrame, das nur die Daten für das Jahr 2018 enthält
df_2018 = df_sum[df_sum['Jahr'] == 2018]
print(df_2018.head())


# Erstellen des Liniendiagramms
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_2013, x='Monat', y='Umsatz', label='2013')
sns.lineplot(data=df_2014, x='Monat', y='Umsatz', label='2014')
sns.lineplot(data=df_2015, x='Monat', y='Umsatz', label='2015')
sns.lineplot(data=df_2016, x='Monat', y='Umsatz', label='2016')
sns.lineplot(data=df_2017, x='Monat', y='Umsatz', label='2017')
sns.lineplot(data=df_2018, x='Monat', y='Umsatz', label='2018')


# Anzeigen des Plots
# plt.show()

# ------------------------------------------




# Erstellen Sie eine Funktion, die das Geschäftsjahr1 basierend auf dem Monat und Jahr berechnet
def berechne_geschaeftsjahr(row):
    if (row['Jahr'] == 2013 and row['Monat'] >= 7) or (row['Jahr'] == 2014 and row['Monat'] <= 6):
        return '2013/14'
    else:
        if (row['Jahr'] == 2014 and row['Monat'] >= 7) or (row['Jahr'] == 2015 and row['Monat'] <= 6):
            return '2014/15'
        else:
            if (row['Jahr'] == 2015 and row['Monat'] >= 7) or (row['Jahr'] == 2016 and row['Monat'] <= 6):
                return '2015/16'
            else:
                if (row['Jahr'] == 2016 and row['Monat'] >= 7) or (row['Jahr'] == 2017 and row['Monat'] <= 6):
                    return '2016/17'
                else:
                    if (row['Jahr'] == 2017 and row['Monat'] >= 7) or (row['Jahr'] == 2018 and row['Monat'] <= 6):
                        return '2017/18'
                    else:
                        return 'sonstiges'

# Erstellen Sie die Geschaeftsjahr1 Spalte
df_sum['Geschaeftsjahr'] = df_sum.apply(berechne_geschaeftsjahr, axis=1)


# print(df_sum.head(50))

# Erstellen des Liniendiagramms
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_sum, x='Monat', y='Umsatz', hue='Geschaeftsjahr')

# Anzeigen des Plots
# plt.show()

# ------------------------------------------

# Summieren Sie den Umsatz für das Geschäftsjahr 2013/14
umsatz_2013_14 = df_sum.loc[df_sum['Geschaeftsjahr'] == '2013/14', 'Umsatz'].sum()

# Ausgeben der Summe des Umsatzes für das Geschäftsjahr 2013/14
print(umsatz_2013_14)



