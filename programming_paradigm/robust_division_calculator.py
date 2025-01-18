def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None

    try:
        result = numerator / denominator
        print(f"The result of the division is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None





        