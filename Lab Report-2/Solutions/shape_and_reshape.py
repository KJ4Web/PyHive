import numpy as np
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
num_sensors = 3
num_timestamps = 4 
required_elements = num_sensors * num_timestamps
if data.size < required_elements:
    padding_needed = required_elements - data.size
    padded_data = np.pad(data, (0, padding_needed), mode='constant', constant_values=0)
    reshaped_array = padded_data.reshape(num_sensors, num_timestamps)
    print()
    print("Original data (padded):", padded_data)
elif data.size > required_elements:
    truncated_data = data[:required_elements]
    reshaped_array = truncated_data.reshape(num_sensors, num_timestamps)
    print("Original data (truncated):", truncated_data)
else:
    reshaped_array = data.reshape(num_sensors, num_timestamps)
    print("Original data:", data)

print("Reshaped 2D array:")
print(reshaped_array)
print()