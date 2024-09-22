import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Check if 'results' directory exists, if not, create it
if not os.path.exists('results'):
    os.makedirs('results')

# Load the cleaned dataset
df = pd.read_csv('data/cleaned_data.csv')

# Check for missing or inconsistent values
print("Missing values in the dataset:\n", df.isnull().sum())

# Plot 1: Distribution of delays
plt.figure(figsize=(10, 6))
sns.histplot(df['DelayMinutes'], bins=30, kde=True)
plt.title('Distribution of Flight Delays (in Minutes)')
plt.xlabel('Delay Minutes')
plt.ylabel('Frequency')
plt.savefig('results/delay_distribution.png')
plt.show()

# Plot 2: Average delay by airline
plt.figure(figsize=(10, 6))
avg_delay_by_airline = df.groupby('Airline')['DelayMinutes'].mean().reset_index()
sns.barplot(x='Airline', y='DelayMinutes', data=avg_delay_by_airline)
plt.title('Average Delay by Airline')
plt.xlabel('Airline')
plt.ylabel('Average Delay (Minutes)')
plt.savefig('results/delay_by_airline.png')
plt.show()

# Plot 3: Relationship between departure time and delays
plt.figure(figsize=(10, 6))
df['DepartureHour'] = pd.to_datetime(df['DepartureTime'], format='%H:%M').dt.hour
sns.lineplot(x='DepartureHour', y='DelayMinutes', data=df)
plt.title('Delays by Departure Time')
plt.xlabel('Departure Hour')
plt.ylabel('Delay Minutes')
plt.savefig('results/delay_by_time.png')
plt.show()


