import numpy as np
score = np.array([85, 90, 78, 92, 88])

indices = np.where(score > 80)
print("Indices of scores > 80:", indices[0])