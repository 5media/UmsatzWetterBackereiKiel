import pandas as pd

# Import Datamerge
from Datamerge_local import merged_df




# Einlesen der merged-Datei 
data = merged_df

print (data.shape)

# Convert to datetime if not already
data['Datum'] = pd.to_datetime(data['Datum'])

# Ensure the data is sorted by date
data = data.sort_values(by='Datum')
print (data.head())


# Define your date thresholds
train_end_date = '2017-07-31'
validation_end_date = '2018-07-31'

# Split the data based on the date thresholds
train_data = data[data['Datum'] <= train_end_date]
validation_data = data[(data['Datum'] > train_end_date) & (data['date'] <= validation_end_date)]
print("Training dataset dimensions:", train_data.shape)
print("Validation dataset dimensions:", validation_data.shape)

