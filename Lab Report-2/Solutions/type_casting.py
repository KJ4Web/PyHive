import numpy as np
data = np.array([
    ["Tuhin", "25", "50000.50"],
    ["Achol", "30", "60000.00"],
    ["Jerin", "35", "70000.75"],
    ["Nur", "40", "80000.00"]])
print("Original data:")
print(data)
print("\nData types before conversion:")
print(data.dtype)
converted_data = np.empty(data.shape, dtype=object)
converted_data[:, 0] = data[:, 0]
converted_data[:, 1] = data[:, 1].astype(int)
converted_data[:, 2] = data[:, 2].astype(float)
print("\nConverted data:")
print(converted_data)
print("\nData types after conversion:")
print(converted_data.dtype)
print()