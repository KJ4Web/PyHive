a = (1, 3, 5, 7, 4)

a_list = list(a)
a_list.insert(2, 400)
a = tuple(a_list)

print("Tuple after adding 400 at index 2:", a)