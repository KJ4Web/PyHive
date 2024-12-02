def concatenate_lists(list1, list2):
    return list1 + list2

list1 = input("Enter the first list: ").split(",")
list2 = input("Enter the second list: ").split(",")

list1 = [item.strip() for item in list1] 
list2 = [item.strip() for item in list2]

result = concatenate_lists(list1, list2)
print("Concatenated list:", result)