def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    """Print all prime numbers in the given interval."""
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()

start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print_primes_in_interval(start, end)