# ===============================
# IMPORT STATEMENTS
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# SINGLE WATER FLOW SENSOR
# ===============================

print("\n--- WATER FLOW SENSOR OUTPUT ---\n")

# Time range: 48 hours, 1-second interval
time_water = pd.date_range(
    start="2025-01-01",
    periods=48 * 60 * 60,
    freq="s"
)

# Base flow (idle state)
flow = np.zeros(len(time_water))

# Usage bursts (tap, shower, washing machine)
for _ in range(40):
    start = np.random.randint(0, len(flow) - 600)
    duration = np.random.randint(30, 600)
    flow[start:start + duration] += np.random.uniform(5, 15)

# Slow leak for 6 hours
leak_start = 10 * 60 * 60
flow[leak_start: leak_start + 6 * 60 * 60] += 0.5

# Sensor noise during flow
noise = np.random.normal(0, 0.2, len(flow))
flow = np.where(flow > 0, flow + noise, 0)

# Create DataFrame
df_water = pd.DataFrame({
    "time": time_water,
    "flow_lpm": flow
})

# Usage event segmentation
df_water["usage_event"] = df_water["flow_lpm"] > 1

# Hourly water usage
hourly_usage = df_water.resample("h", on="time")["flow_lpm"].sum()

# Leak detection (sustained low flow)
df_water["leak"] = (df_water["flow_lpm"] > 0.2) & (df_water["flow_lpm"] < 1)

# Usage pattern classification
conditions = [
    df_water["flow_lpm"] > 10,
    df_water["flow_lpm"].between(3, 10),
    df_water["flow_lpm"].between(0.2, 3)
]
labels = ["High", "Medium", "Low"]

df_water["usage_type"] = np.select(conditions, labels, default="Idle")

# Leakage impact report
leak_volume = df_water[df_water["leak"]]["flow_lpm"].sum()

print("Total water used per hour (first 5 hours):")
print(hourly_usage.head())

print("\nTotal water lost due to leakage:", round(leak_volume, 2), "litres")

# Visualization
plt.figure()
df_water.set_index("time")["flow_lpm"].resample("h").mean().plot()
plt.title("Hourly Average Water Flow")
plt.xlabel("Time")
plt.ylabel("Flow (LPM)")
plt.show()