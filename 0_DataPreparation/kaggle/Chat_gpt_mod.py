# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# File paths
train_path = 'train.csv'
test_path = 'test.csv'
submission_path = 'sample_submission.csv'
wetter_path = 'wetter.csv'

# Load data
train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)
submission_df = pd.read_csv(submission_path)
weather_df = pd.read_csv(wetter_path)


# Convert 'Datum' to datetime
train_df['Datum'] = pd.to_datetime(train_df['Datum'])
test_df['Datum'] = pd.to_datetime(test_df['Datum'])
weather_df['Datum'] = pd.to_datetime(weather_df['Datum'])

# Merge weather data with training data
train_df = pd.merge(train_df, weather_df, on='Datum', how='left')

# Handle missing values in weather data (e.g., fill with mean or median)
train_df['Wettercode'].fillna(train_df['Wettercode'].mean(), inplace=True)

# Feature engineering: extract time-based features
train_df['Wochentag'] = train_df['Datum'].dt.weekday
train_df['Monat'] = train_df['Datum'].dt.month
train_df['Jahr'] = train_df['Datum'].dt.year

test_df['Wochentag'] = test_df['Datum'].dt.weekday
test_df['Monat'] = test_df['Datum'].dt.month
test_df['Jahr'] = test_df['Datum'].dt.year

# Verify new features
print(train_df.head(), test_df.head())

# Define features and target variable
features = ['Warengruppe', 'Wochentag', 'Monat', 'Jahr', 'Bewoelkung', 'Temperatur', 'Windgeschwindigkeit', 'Wettercode']
target = 'Umsatz'

# Separate features and target variable in the training set
X_train = train_df[features]
y_train = train_df[target]

X_test = test_df[features]

# Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Verify scaled features
print(X_train_scaled[:5], X_test_scaled[:5])

# Build the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mse')

# Train the model
history = model.fit(X_train_scaled, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Plot training history
plt.figure(figsize=(12, 6))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss During Training')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Make predictions on the test set
predictions = model.predict(X_test_scaled)

# Save predictions to sample_submission.csv
submission_df['Umsatz'] = predictions
submission_df.to_csv('Vorhersage.csv', index=False)

# Display the first few rows of the submission file
print(submission_df.head())
