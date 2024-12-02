def list_to_set(lst):
    return set(lst)

elements = input("Enter a list: ").split(",")
elements = [item.strip() for item in elements]

result_set = list_to_set(elements)
print("Converted set:", result_set)