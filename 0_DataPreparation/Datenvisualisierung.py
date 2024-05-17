import pandas as pd
import matplotlib.pyplot as plt


# Assuming your CSV files are named kiwo.csv, umsatz.csv, and wetter.csv

# Load CSV files into pandas DataFrames
df1 = pd.read_csv('test_repo/0_DataPreparation/kiwo.csv')
df2 = pd.read_csv('test_repo/0_DataPreparation/umsatzdaten_gekuerzt.csv')
df3 = pd.read_csv('test_repo/0_DataPreparation/wetter.csv')



# Print the first few rows of each DataFrame to verify the import
print("First few rows of kiwo.csv:")
print(df1.head())

print("\nFirst few rows of umsatz.csv:")
print(df2.head())

print("\nFirst few rows of wetter.csv:")
print(df3.head())


df3.plot.scatter('Datum', # x-axis
                'Temperatur', # y-axis
                grid=False, # Add a grid in the background
               )
plt.show()

