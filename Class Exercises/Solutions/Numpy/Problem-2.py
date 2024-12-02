import numpy as np
score = np.array([85, 90, 78, 92, 88])

a_score = score.copy()
a_score += 5
print("Original score:", score)
print("Modified a_score:", a_score)