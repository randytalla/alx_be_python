num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Choose the operation (+, -, *, /): ")

match operation: 
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        print(f"The result is {num1 / num2}")
    case _:
        print("Invalid operation. Please choose from +, -, *, /")