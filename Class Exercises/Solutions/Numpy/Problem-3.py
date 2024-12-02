import numpy as np
score = np.array([85, 90, 78, 92, 88])

print("Shape:", score.shape)
print("Number of dimensions:", score.ndim)
print("Size:", score.size)
print("Item size:", score.itemsize)
print("Data type:", score.dtype)
print("Sorted scores:", np.sort(score))