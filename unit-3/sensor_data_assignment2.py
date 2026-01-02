# ===============================
# IMPORT STATEMENTS
# ===============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# SINGLE HEART RATE SENSOR
# ===============================

print("\n--- HEART RATE SENSOR OUTPUT ---\n")

# Time range: 24 hours, 5-second sampling interval
time_hr = pd.date_range(
    start="2025-01-01",
    periods=24 * 60 * 60 // 5,
    freq="5s"
)

# Baseline heart rate
heart_rate = np.random.normal(70, 5, len(time_hr))

# Sleep period (first 6 hours)
sleep_samples = 6 * 60 * 60 // 5
heart_rate[:sleep_samples] -= 15

# Exercise sessions
exercise_starts = [3000, 8000, 12000]
for start in exercise_starts:
    # Exercise phase
    heart_rate[start:start + 600] += 50
    # Recovery phase
    heart_rate[start + 600:start + 1200] -= np.linspace(50, 0, 600)

# Dropouts during motion
drop_idx = np.random.choice(len(heart_rate), 100, replace=False)
heart_rate[drop_idx] = np.nan

# Create DataFrame
df_hr = pd.DataFrame({
    "time": time_hr,
    "heart_rate": heart_rate
})

# ===============================
# PANDAS TASKS
# ===============================

# 1. Sleep and active period inference
df_hr["state"] = np.where(df_hr["heart_rate"] < 60, "Sleep", "Active")

# 2. Exercise session detection
df_hr["exercise"] = df_hr["heart_rate"] > 120

# 3. Recovery time calculation (heart rate back to normal range)
df_hr["recovery"] = df_hr["heart_rate"].between(70, 90)

# 4. Abnormal heart rate detection
df_hr["abnormal"] = (df_hr["heart_rate"] > 160) | (df_hr["heart_rate"] < 40)

# 5. Daily fitness summary table
fitness_summary = df_hr.groupby("state")["heart_rate"].mean()

print("Daily Fitness Summary (Average Heart Rate):")
print(fitness_summary)

# ===============================
# VISUALIZATION
# ===============================

plt.figure()
df_hr.set_index("time")["heart_rate"].plot()
plt.title("Heart Rate Over 24 Hours")
plt.xlabel("Time")
plt.ylabel("Heart Rate (BPM)")
plt.show()