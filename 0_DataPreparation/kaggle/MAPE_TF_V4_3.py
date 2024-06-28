import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Daten einlesen
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
kiwo_df = pd.read_csv('kiwo.csv')
wetter_df = pd.read_csv('wetter.csv')

# Convert date columns to datetime format
train_df['Datum'] = pd.to_datetime(train_df['Datum'])
test_df['Datum'] = pd.to_datetime(test_df['Datum'])
wetter_df['Datum'] = pd.to_datetime(wetter_df['Datum'])
kiwo_df['Datum'] = pd.to_datetime(kiwo_df['Datum'])

# Merge the datasets
train_df = pd.merge(train_df, wetter_df, on='Datum', how='left')
test_df = pd.merge(test_df, wetter_df, on='Datum', how='left')

train_df = pd.merge(train_df, kiwo_df, on='Datum', how='left')
test_df = pd.merge(test_df, kiwo_df, on='Datum', how='left')

train_df['KielerWoche'] = train_df['KielerWoche'].fillna(0)
test_df['KielerWoche'] = test_df['KielerWoche'].fillna(0)

# Handle missing values in weather-related columns
for col in ['Bewoelkung', 'Temperatur', 'Windgeschwindigkeit', 'Wettercode']:
    train_df[col] = train_df[col].fillna(train_df[col].mean())
    test_df[col] = test_df[col].fillna(test_df[col].mean())

# Feature engineering: Extract additional features from the date column
def extract_date_features(df):
    df['Year'] = df['Datum'].dt.year
    df['Month'] = df['Datum'].dt.month
    df['Day'] = df['Datum'].dt.day
    df['DayOfWeek'] = df['Datum'].dt.dayofweek
    df['WeekOfYear'] = df['Datum'].dt.isocalendar().week
    df['Quarter'] = df['Datum'].dt.quarter
    return df

train_df = extract_date_features(train_df)
test_df = extract_date_features(test_df)

# Define features and target variable
features = ['Bewoelkung', 'Temperatur', 'Windgeschwindigkeit', 'Wettercode', 
            'KielerWoche', 'Year', 'Month', 'Day', 'DayOfWeek', 'WeekOfYear', 'Quarter']
target = 'Umsatz'

# Normalize the data
scaler = StandardScaler()

# MAPE Berechnung für jede Warengruppe
warengruppen = train_df['Warengruppe'].unique()
mape_dict = {}

for warengruppe in warengruppen:
    # Filter data for the current Warengruppe
    train_grp = train_df[train_df['Warengruppe'] == warengruppe]
    
    if train_grp.empty:
        continue
    
    X = train_grp[features]
    y = train_grp[target]
    
    X = scaler.fit_transform(X)
    
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Build the neural network model
    model = Sequential([
        Dense(128, input_dim=X_train.shape[1], activation='relu'),
        Dropout(0.2),
        BatchNormalization(),
        Dense(64, activation='relu'),
        Dropout(0.2),
        BatchNormalization(),
        Dense(32, activation='relu'),
        Dropout(0.2),
        BatchNormalization(),
        Dense(1)
    ])
    
    model.compile(loss="mse", optimizer='adam')
    #model.compile(loss="mse", optimizer=Adam (learning_rate=0.001))
    
    history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=90, batch_size=32, verbose=0)
    
    y_pred = model.predict(X_val)
    mape = mean_absolute_percentage_error(y_val, y_pred)
    
    mape_dict[warengruppe] = mape

# Gesamten MAPE berechnen
X_all = train_df[features]
y_all = train_df[target]

X_all = scaler.fit_transform(X_all)

X_train_all, X_val_all, y_train_all, y_val_all = train_test_split(X_all, y_all, test_size=0.2, random_state=42)

model_all = Sequential([
    Dense(128, input_dim=X_train_all.shape[1], activation='relu'),
    Dropout(0.2),
    BatchNormalization(),
    Dense(64, activation='relu'),
    Dropout(0.2),
    BatchNormalization(),
    Dense(32, activation='relu'),
    Dropout(0.2),
    BatchNormalization(),
    Dense(1)
])

model_all.compile(loss="mse", optimizer='adam')

history_all = model_all.fit(X_train_all, y_train_all, validation_data=(X_val_all, y_val_all), epochs=50, batch_size=32, verbose=0)

y_pred_all = model_all.predict(X_val_all)
mape_all = mean_absolute_percentage_error(y_val_all, y_pred_all)

print(f'Gesamter MAPE: {mape_all}')
print(f'MAPE für jede Warengruppe: {mape_dict}')
