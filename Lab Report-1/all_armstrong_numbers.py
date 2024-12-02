def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
    return num == armstrong_sum

def find_armstrong_numbers_in_interval(start, end):
    print(f"Armstrong numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            print(num, end=" ")
    print()

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

find_armstrong_numbers_in_interval(start, end)