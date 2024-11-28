import numpy as np
scores = np.array([85, 70, 90, 75, 60, 95, 80, 100, 55, 88])
search_scores = [75, 90]
indices = {score: np.where(scores == score)[0] for score in search_scores}
print("Indices of specific scores:")
for score, idx in indices.items():
    if idx.size > 0:
        print(f"Score {score} found at indices: {idx}")
    else:
        print(f"Score {score} not found.")
sorted_ascending = np.sort(scores)
print("\nScores sorted in ascending order:")
print(sorted_ascending)
sorted_descending = np.sort(scores)[::-1]  
print("\nScores sorted in descending order:")
print(sorted_descending)