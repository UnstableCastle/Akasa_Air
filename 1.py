import pandas as pd
import os

# Load the dataset
df = pd.read_csv('aviation_data.csv')

# Normalize date formats to YYYY-MM-DD
df['DepartureDate'] = pd.to_datetime(df['DepartureDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
df['ArrivalDate'] = pd.to_datetime(df['ArrivalDate'], format='%m/%d/%Y').dt.strftime('%Y-%m-%d')

# Convert time to 24-hour format
df['DepartureTime'] = pd.to_datetime(df['DepartureTime'], format='%I:%M %p').dt.strftime('%H:%M')
df['ArrivalTime'] = pd.to_datetime(df['ArrivalTime'], format='%I:%M %p').dt.strftime('%H:%M')

# Fill missing values in DelayMinutes with the median delay
df['DelayMinutes'] = df['DelayMinutes'].fillna(df['DelayMinutes'].median())

# Remove duplicate entries based on FlightNumber, DepartureDate, and DepartureTime
df.drop_duplicates(subset=['FlightNumber', 'DepartureDate', 'DepartureTime'], inplace=True)

# Calculate FlightDuration 
df['FlightDuration'] = pd.to_datetime(df['ArrivalTime'], format='%H:%M') - pd.to_datetime(df['DepartureTime'], format='%H:%M')

# Check if 'data' directory exists, if not, create it
if not os.path.exists('data'):
    os.makedirs('data')

# Save the cleaned and normalized dataset
df.to_csv('data/cleaned_data.csv', index=False)

print('--End --')
