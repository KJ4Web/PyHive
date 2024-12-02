def print_fibonacci_sequence(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    print("Fibonacci Sequence:")
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

n_terms = int(input("Enter the number of terms: "))
print_fibonacci_sequence(n_terms)