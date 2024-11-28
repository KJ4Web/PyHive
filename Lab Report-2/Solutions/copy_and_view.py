import numpy as np
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])
print("Original array:")
print(data) 
row_view = data[1] 
print("\nView of the second row:")
print(row_view) 
column_copy = data[:, 0].copy() 
print("\nDeep copy of the first column:")
print(column_copy)
row_view[0] = 100  
print("\nModified view of the second row:")
print(row_view)
column_copy[0] = 200 
print("\nModified copy of the first column:")
print(column_copy)
print("\nOriginal array after modifications:")
print(data)