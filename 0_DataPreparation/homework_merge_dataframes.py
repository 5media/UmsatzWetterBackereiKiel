import pandas as pd

# Assuming your CSV files are named kiwo.csv, umsatz.csv, and wetter.csv

# Load CSV files into pandas DataFrames
df1 = pd.read_csv('kiwo.csv')
df2 = pd.read_csv('umsatzdaten_gekuerzt.csv')
df3 = pd.read_csv('wetter.csv')

# Print the first few rows of each DataFrame to verify the import
print("First few rows of kiwo.csv:")
print(df1.head())

print("\nFirst few rows of umsatz.csv:")
print(df2.head())

print("\nFirst few rows of wetter.csv:")
print(df3.head())

# Merge df1 and df2 by 'Datum'
merged_df = pd.merge(df1, df2, on='Datum')

# Merge the result with df3 by 'Datum'
merged_df = pd.merge(merged_df, df3, on='Datum')

# Print the resulting merged DataFrame
print(merged_df)

# Variablen erstellen

# Variable Umsatz-Temperatur

# Variable Umsatz-Wind

# Durchschnitt-Temperatur

# Durchschnitt-Wind

# Durchscnitt-Umsatz


