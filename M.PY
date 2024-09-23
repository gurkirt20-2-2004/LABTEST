import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Set random seed for reproducibility
np.random.seed(0)

# Generate noisy vehicle count data
vc = np.random.poisson(40, 1440) + np.random.normal(0, 10, 1440)

# Apply a Butterworth filter to smooth the data
b, a = butter(3, 0.05)
vc_smooth = filtfilt(b, a, vc)

# Calculate hourly average
h_avg = np.mean(vc.reshape(24, 60), axis=1)
print("Hourly average is:", h_avg)

# Plot the noisy and smoothed data
plt.figure(figsize=(12, 6))
plt.plot(vc, label="Noisy Data", alpha=0.5)
plt.plot(vc_smooth, label="Smooth Data")
plt.xlabel('Minutes')
plt.ylabel('Vehicle Count')
plt.title('Vehicle Count Data')
plt.legend()
plt.show()

# Function to detect congestion
def conj(vc, threshold=120, duration=15):
    conge = []
    cnt = 0
    for i in range(len(vc)):
        if vc[i] > threshold:
            cnt += 1
            if cnt >= duration:
                conge.append(i)  # Fixed typo here (from eppend to append)
        else:
            cnt = 0
    return conge

# Detect congestions
cong_p = conj(vc)
print("Congestions are at indices:", cong_p)

# Plot the congestions
plt.figure(figsize=(12, 6))
plt.plot(vc, label="Vehicle Count", alpha=0.5)
plt.scatter(cong_p, vc[cong_p], color='red', label='Congestions', alpha=0.8)
plt.xlabel('Minutes')
plt.title('Congestion Points')
plt.legend()
plt.show()




