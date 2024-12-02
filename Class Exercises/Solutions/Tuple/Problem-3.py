a = (1, 3, 5, 7, 4)

odd_count = sum(1 for x in a if x % 2 != 0)
even_count = sum(1 for x in a if x % 2 == 0)

print("Total odd numbers:", odd_count)
print("Total even numbers:", even_count)