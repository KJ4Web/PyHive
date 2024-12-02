a = [1, 3, 5, 7, 9]

new_list = [2, 4, 6]
a.extend(new_list)
print("After joining new list: ", a)

b = a.copy()
print("Copied list b:", b)