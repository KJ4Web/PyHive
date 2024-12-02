import numpy as np
score = np.array([85, 90, 78, 92, 88])

score = score.astype(float)
print("Scores as float:", [f"{x:.2f}" for x in score])