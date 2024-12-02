def compare_lists(list1, list2):
    return list1 == list2

list1 = input("Enter the first list: ").split(",")
list2 = input("Enter the second list: ").split(",")

list1 = [item.strip() for item in list1]
list2 = [item.strip() for item in list2]

if compare_lists(list1, list2):
    print("The lists are equal.")
else:
    print("The lists are not equal.")