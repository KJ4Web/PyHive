def reverse_string(s):
    return s[::-1]

user_input = input("Enter a string: ")

reversed_string = reverse_string(user_input)
print(f"The reverse of '{user_input}' is '{reversed_string}'.")