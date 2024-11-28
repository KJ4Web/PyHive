def divide_elements(values, divisor):
    if not isinstance(divisor, (int, float)):
        raise TypeError("The divisor must be a numeric value (int or float).")
    results = []
    for value in values:
        try:
            result = value / divisor
            results.append(result)
        except ZeroDivisionError:
            print(f"Error: Cannot divide {value} by zero.")
            results.append(None)  
        except Exception as e:
            print(f"Unexpected error when processing {value}: {e}")
            results.append(None)  
    return results
values = [10, 20, 30, 0, 40]
divisor = 0 
try:
    results = divide_elements(values, divisor)
    print("Results:", results)
except TypeError as te:
    print(te)