a = {1, 3, 5, 8, 3, 7}
b = {0, False, 1, 5}

union = a.union(b)
print("Union of a and b:", union)

intersection = a.intersection(b)
print("Intersection of a and b:", intersection)

difference = a.difference(b)
print("Difference of a and b (a - b):", difference)

symmetric_difference = a.symmetric_difference(b)
print("Symmetric difference of a and b:", symmetric_difference)

subset = a.issubset(b)
print("Is a a subset of b?:", subset)