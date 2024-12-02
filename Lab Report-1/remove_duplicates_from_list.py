def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

elements = input("Enter a list: ").split(",")
elements = [item.strip() for item in elements]

unique_elements = remove_duplicates(elements)
print("List after removing duplicates:", unique_elements)