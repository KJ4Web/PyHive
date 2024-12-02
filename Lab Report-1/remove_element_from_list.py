def remove_element_from_list(lst, element):
    try:
        lst.remove(element)
        print(f"'{element}' has been removed.")
    except ValueError:
        print(f"'{element}' is not in the list.")

my_list = input("Enter elements of the list separated by commas: ").split(",")
my_list = [item.strip() for item in my_list]  # Clean up extra spaces

element_to_remove = input("Enter the element to remove: ")

remove_element_from_list(my_list, element_to_remove)

print("Updated list:", my_list)