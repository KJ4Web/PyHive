def calculate_expression(a, b):
    return a**2 + b**2 + 2*a*b

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
result = calculate_expression(a, b)
print(f"The result of (a+b)^2 is: {result}")