import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


wetter_url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/wetter.csv"
kiwo_url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/kiwo.csv"
umsaetze_url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/umsatzdaten_gekuerzt.csv"
wetter_df = pd.read_csv(wetter_url)
kiwo_df = pd.read_csv(kiwo_url)
umsaetze_df = pd.read_csv(umsaetze_url)
#plt.bar(categories, values)

# Ausgeben der ersten Zeilen der Umsatzdaten
print(umsaetze_df.head())

# Konvertiere die 'Datum' Spalte in ein datetime-Objekt (?)
umsaetze_df['Datum'] = pd.to_datetime(umsaetze_df['Datum']) 

# Initialisieren des Dictionary vor der Schleife, Erstellen eines leeren Dictionary
mean_Wochentage_d={} 

# Hinzufügen der Spalte "Wochentag"
umsaetze_df["Wochentag"]=umsaetze_df["Datum"].dt.weekday 

# Schleife, schrittweises Definieren der Einträge im Dictionary
for i in range(7): 
    mean_Wochentage_d[i]=umsaetze_df["Umsatz"][umsaetze_df["Wochentag"]==i].mean() 

# Umwandeln des Dictionarys in eine Liste
mean_Wochentage = list(mean_Wochentage_d.values()) 
print(mean_Wochentage)

## Balkendiagramm ohne Konfidenzintervalle
#Erstellen des Balkendiagramms zum durchschnittlichen Umsatz je Wochentag
fig,ax = plt.subplots()
ax.bar(["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"], mean_Wochentage)
ax.set_title("Durchschnittlicher Umsatz je Wochentag")
ax.set_xlabel("Wochentage")
ax.set_ylabel("Durchschnittlicher Umsatz")


## Balkendiagramm mit Konfidenzintervallen
# Erstellen der Konfidenzintervalle auf dem Balkendiagramm
# Ziel: Zu 95% soll der wahre Mittelwert mean für einen Wochentag i aus Mo, .., So im Intervall liegen

# Berechnung der Standardfehler und Konfidenzintervalle
standard_errors = []
for i in range(7):
    data = umsaetze_df["Umsatz"][umsaetze_df["Wochentag"] == i]
    standard_error = stats.sem(data)  # Standardfehler des Mittels
    standard_errors.append(standard_error)


# Berechnung der 95%-Konfidenzintervalle
conf_intervals = [1.96 * se for se in standard_errors]

# Erstellen des Balkendiagramms zum durchschnittlichen Umsatz je Wochentag
fig, ax = plt.subplots()
categories = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

# Erstellen des Balkendiagramms mit Konfidenzintervallen
ax.bar(categories, mean_Wochentage, yerr=conf_intervals, capsize=5, color='skyblue', edgecolor='black', linewidth=1.2)
ax.set_title("Durchschnittlicher Umsatz je Wochentag")
ax.set_xlabel("Wochentage")
ax.set_ylabel("Durchschnittlicher Umsatz")

# Mittelwerte auf den Balken anzeigen
for i, mean in enumerate(mean_Wochentage):
    ax.text(i, mean + conf_intervals[i] + 0.5, f'{mean:.2f}', ha='center')

# Diagramm anzeigen
plt.show()