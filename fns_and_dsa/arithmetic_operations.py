def perform_operation (num1:float, num2:float, operation:str):
    if operation == "add":
        return num1 + num2
    elif operation == "subract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"
        else:
            return "Error: Invalid operation"


# if __name__ == "__main__":
#     result = perform_operation(0,10,"divide")
#     print(f"Result: {result}")
