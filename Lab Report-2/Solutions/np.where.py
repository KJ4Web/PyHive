import numpy as np
temperatures = np.array([15, 22, 18, 30, 25, 10, 5, 28, 20, 35])
high_temp_threshold = 25
high_temp_indices = np.where(temperatures > high_temp_threshold)[0]
print()
print("Indices where temperature exceeds the threshold of 25°C:", high_temp_indices)
min_temp_value = 10
updated_temperatures = np.where(temperatures < 15, min_temp_value, temperatures)
print("\nUpdated temperatures:")
print(updated_temperatures)