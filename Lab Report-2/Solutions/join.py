import numpy as np
a = np.array([100, 200, 150, 300, 250]) 
b = np.array([120, 180, 160, 290, 270]) 
horizontal_join = np.column_stack((a, b))
print("Horizontal Join (as columns):")
print(horizontal_join)
vertical_join = np.vstack((a, b))
print("\nVertical Join (as additional rows):")
print(vertical_join)