a = (1, 3, 5, 7, 4)

print("Printing tuple and skipping 5:")

for value in a:
    if value == 5:
        continue
    print(value)