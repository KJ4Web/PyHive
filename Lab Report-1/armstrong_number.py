def is_armstrong_number(num):
    """Check if a number is an Armstrong number."""
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
    return num == armstrong_sum

number = int(input("Enter a number to check if it's an Armstrong number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")