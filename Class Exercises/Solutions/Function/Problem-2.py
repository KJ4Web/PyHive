lambda_expression = lambda a, b: a**2 + b**2 + 2*a*b

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
result = lambda_expression(a, b)
print(f"The result of (a+b)^2 using lambda is: {result}")