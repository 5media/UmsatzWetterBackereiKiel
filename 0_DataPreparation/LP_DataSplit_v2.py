import pandas as pd

# Import Datamerge
from Datamerge_local import merged_df




# Einlesen der merged-Datei 
data = merged_df

print (data.shape)






# Konvertieren Sie die Spaltenwerte in datetime, falls noch nicht geschehen
data['Datum'] = pd.to_datetime(data['Datum'])

# Erstellen Sie die Grenzen für die Trainings- und Validierungsdatensätze
train_start = pd.to_datetime('2013-07-01')
train_end = pd.to_datetime('2017-07-31')
validation_start = pd.to_datetime('2017-08-01')
validation_end = pd.to_datetime('2018-07-31')

# Teilen Sie die Daten in Trainings- und Validierungsdatensätze auf
train_data = data[(data['Datum'] >= train_start) & (data['Datum'] <= train_end)]
validation_data = data[(data['Datum'] >= validation_start) & (data['Datum'] <= validation_end)]


print ("Training dataset dimensions:", train_data.shape)
print ("Validation dataset dimensions:", validation_data.shape)
