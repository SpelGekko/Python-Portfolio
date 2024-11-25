## Made by Gekko

import requests
import json
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Get API key from .env file --> Security best practice
load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")
# API endpoint --> Otherwise it wont work 
url = f"https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0"

# Get data from API 
response = requests.get(url)
data = response.json()

# Initialize lists to store data for plotting --> We use lists to store the data for plotting
sols = []
avg_temps = []
max_temps = []
min_temps = []
wind_speeds = []
pressures = []

# Process and collect data for visualization
if 'sol_keys' in data:
    sol_keys = data['sol_keys']
    for sol in sol_keys:
        sol_data = data[sol]
        sols.append(sol)
        avg_temps.append(sol_data['AT']['av'])
        max_temps.append(sol_data['AT']['mx'])
        min_temps.append(sol_data['AT']['mn'])
        wind_speeds.append(sol_data['HWS']['av'])
        pressures.append(sol_data['PRE']['av'])
else:
    print("No data available")

# Plot the data using matplotlib 
plt.figure(figsize=(10, 8))

# Plot temperatures
plt.subplot(3, 1, 1)
plt.plot(sols, avg_temps, marker='o', label='Average Temperature')
plt.plot(sols, max_temps, marker='o', label='Max Temperature', color='red')
plt.plot(sols, min_temps, marker='o', label='Min Temperature', color='blue')
plt.title('Mars Weather Data')
plt.ylabel('Temperature (°C)')
plt.legend()

# Plot wind speeds
plt.subplot(3, 1, 2)
plt.plot(sols, wind_speeds, marker='o')
plt.ylabel('Wind Speed (m/s)')

# Plot pressures
plt.subplot(3, 1, 3)
plt.plot(sols, pressures, marker='o')
plt.xlabel('Sol')
plt.ylabel('Pressure (Pa)')

plt.tight_layout()
plt.show()