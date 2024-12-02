def list_to_string(lst, delimiter=" "):
    return delimiter.join(lst)

elements = input("Enter a list: ").split(",")
elements = [item.strip() for item in elements]

result_string = list_to_string(elements, delimiter=" ")
print("Converted string:", result_string)