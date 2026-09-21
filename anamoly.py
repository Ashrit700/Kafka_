import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Create sample log dataset
# --------------------------------------------------

data = {
    "Timestamp": pd.date_range("2026-09-21 09:00:00", periods=15, freq="min"),

    "CPU Usage": [
        45, 52, 48, 55, 51,
        49, 53, 95, 50, 47,
        54, 92, 48, 51, 49
    ],

    "Memory Usage": [
        60, 62, 61, 63, 65,
        64, 62, 95, 63, 61,
        64, 94, 62, 63, 61
    ],

    "Response Time": [
        120, 130, 125, 135, 128,
        132, 129, 800, 130, 125,
        135, 750, 128, 132, 127
    ]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# 2. Display dataset
# --------------------------------------------------

print("\n===== LOG DATASET =====")
print(df)

# --------------------------------------------------
# 3. Calculate basic statistics
# --------------------------------------------------

print("\n===== BASIC STATISTICS =====")
print(df[["CPU Usage", "Memory Usage", "Response Time"]].describe())

# --------------------------------------------------
# 4. Define anomaly thresholds
# --------------------------------------------------

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
RESPONSE_TIME_THRESHOLD = 500

# --------------------------------------------------
# 5. Detect anomalies
# --------------------------------------------------

df["CPU Anomaly"] = df["CPU Usage"] > CPU_THRESHOLD

df["Memory Anomaly"] = df["Memory Usage"] > MEMORY_THRESHOLD

df["Response Time Anomaly"] = (
    df["Response Time"] > RESPONSE_TIME_THRESHOLD
)

# A record is anomalous if ANY metric crosses its threshold
df["Anomaly"] = (
    df["CPU Anomaly"]
    | df["Memory Anomaly"]
    | df["Response Time Anomaly"]
)

# --------------------------------------------------
# 6. Print anomalous records
# --------------------------------------------------

anomalies = df[df["Anomaly"]]

print("\n===== ANOMALOUS RECORDS =====")

if anomalies.empty:
    print("No anomalies detected.")

else:
    print(
        anomalies[
            [
                "Timestamp",
                "CPU Usage",
                "Memory Usage",
                "Response Time"
            ]
        ]
    )

# --------------------------------------------------
# 7. Display anomaly count
# --------------------------------------------------

print("\nTotal anomalies detected:", len(anomalies))

# --------------------------------------------------
# 8. Plot metrics and anomalies
# --------------------------------------------------

plt.figure(figsize=(12, 8))

# CPU
plt.subplot(3, 1, 1)

plt.plot(
    df["Timestamp"],
    df["CPU Usage"],
    marker="o",
    label="CPU Usage"
)

plt.axhline(
    CPU_THRESHOLD,
    linestyle="--",
    label="CPU Threshold"
)

plt.scatter(
    df.loc[df["CPU Anomaly"], "Timestamp"],
    df.loc[df["CPU Anomaly"], "CPU Usage"],
    marker="x",
    s=100,
    label="CPU Anomaly"
)

plt.ylabel("CPU (%)")
plt.title("CPU Usage")
plt.legend()

# Memory
plt.subplot(3, 1, 2)

plt.plot(
    df["Timestamp"],
    df["Memory Usage"],
    marker="o",
    label="Memory Usage"
)

plt.axhline(
    MEMORY_THRESHOLD,
    linestyle="--",
    label="Memory Threshold"
)

plt.scatter(
    df.loc[df["Memory Anomaly"], "Timestamp"],
    df.loc[df["Memory Anomaly"], "Memory Usage"],
    marker="x",
    s=100,
    label="Memory Anomaly"
)

plt.ylabel("Memory (%)")
plt.title("Memory Usage")
plt.legend()

# Response Time
plt.subplot(3, 1, 3)

plt.plot(
    df["Timestamp"],
    df["Response Time"],
    marker="o",
    label="Response Time"
)

plt.axhline(
    RESPONSE_TIME_THRESHOLD,
    linestyle="--",
    label="Response Time Threshold"
)

plt.scatter(
    df.loc[df["Response Time Anomaly"], "Timestamp"],
    df.loc[df["Response Time Anomaly"], "Response Time"],
    marker="x",
    s=100,
    label="Response Time Anomaly"
)

plt.ylabel("Response Time (ms)")
plt.xlabel("Timestamp")
plt.title("Response Time")
plt.legend()

plt.tight_layout()
plt.show()