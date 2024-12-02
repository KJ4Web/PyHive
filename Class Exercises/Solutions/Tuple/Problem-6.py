a = (1, 3, 5, 7, 4)

a_list = list(a)
a_list.pop()
a = tuple(a_list)
print("Tuple after removing the last element:", a)