# =============================
# Simulation of sensor data
# =============================

import random
import time

for i in range(10):
    t_c = 25 + random.uniform(-2, 2)  # temperature in degree Celsius
    print(f"Temperature: {t_c:.2f} °C")
    time.sleep(0.1)  # pause for 0.1 seconds


# =============================
# Simulate a virtual sensor
# =============================

import random as r
import time
import csv

with open('sensor_read.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'Temperature_C'])  # fixed header

    for i in range(10):
        ts = time.time()  # Unix timestamp
        t_c = 25 + r.uniform(-2, 2)
        writer.writerow([ts, f'{t_c:.2f}'])
        print(f"Timestamp: {ts}, Temperature: {t_c:.2f} °C")
        time.sleep(0.1)


# =============================
# Visualization of the readings
# =============================

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv('sensor_read.csv')
print(df.shape)

# Convert columns to numeric
df['Timestamp'] = pd.to_numeric(df['Timestamp'], errors='coerce')
df['Temperature_C'] = pd.to_numeric(df['Temperature_C'], errors='coerce')

# Convert timestamp to datetime
df['Datetime'] = pd.to_datetime(df['Timestamp'], unit='s')

print(df.dtypes)
print(df.head())

# =============================
# Smooth the sensor data
# =============================

df['Temperature_Smooth'] = df['Temperature_C'].rolling(window=3).mean()

# =============================
# Plotting
# =============================

plt.figure()
plt.plot(df['Datetime'], df['Temperature_C'], label='Raw Data', alpha=0.6)
plt.plot(df['Datetime'], df['Temperature_Smooth'], label='Smoothed Data', linewidth=2)

plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.title('Sensor Temperature Readings Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# =============================
# Mean comparison
# =============================

mid_index = len(df) // 2
first_half_mean = df['Temperature_Smooth'].iloc[:mid_index].mean()
second_half_mean = df['Temperature_Smooth'].iloc[mid_index:].mean()

print(f'Mean of first half: {first_half_mean:.2f}')
print(f'Mean of second half: {second_half_mean:.2f}')


