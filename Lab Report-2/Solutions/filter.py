import numpy as np
product_prices = np.array([15.99, 22.50, 30.00, 45.75, 50.00, 60.00, 75.25, 10.00, 40.00])
lower_bound = 20.00
upper_bound = 50.00
filtered_prices = product_prices[(product_prices >= lower_bound) & (product_prices <= upper_bound)]
print("Filtered product prices within the range $20 to $50:")
print(filtered_prices)