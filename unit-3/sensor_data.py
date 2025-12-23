#simulation of sensor data
import random
import time


for i in range(10):
    t_c=25+random.uniform(-2,2)  #temperature in degree celsius
    print(f"Temperature: {t_c:.2f} °C")
    time.sleep(0.1)#it will pause the execution for 1 second

#simulate a virtual sensor
import random as r
import time
import csv

with open('sensor_read.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp', 'Temperature_C', 'Humidity_%'])
    #column headers are created for csv file
    for i in range(10):
        ts=time.time()
        #current time is captured in seconds from unix epach time
        t_c=25 + r.uniform(-2,2)
        writer.writerow([ts, f'{t_c:.2f}'])
        print(f"Timestamp: {ts}, Temperature: {t_c:.2f} °C")
        time.sleep(0.1)  #pause for half second before next reading
        print(ts,t_c)
        
        
#Visulaizarion of the readings
#interpret the data and visualize
import pandas as pd
import matplotlib.pyplot as plt

#create the dataframe from the readings
df=pd.read_csv('sensor_read.csv')
print(df.shape)


#convert the string to a numeric data
df['Timestamp']=pd.to_numeric(df['Timestamp'], errors='coerce')
df['Temperature_C']=pd.to_numeric(df['Temperature_C'], errors='coerce')
df['value']=pd.to_datetime(df['Temperature_C'], errors='coerce')


print(df.dtypes)


#convert timestamp to datetime
df['Datetime']=pd.to_datetime(df['Timestamp'], unit='s')
print(df.dtypes)
print(df.head())


print(plt.figure())

print(plt.plot(df['Timestamp'], df['Temperature_C']))
#a line graph is drawn


print(plt.xlabel('Timestamp'))
print(plt.ylabel('Temperature (°C)'))
print(plt.title('Sensor Temperature Readings Over Time'))

print(plt.show())
plt.xticks(rotation=45)
print(plt.show())


