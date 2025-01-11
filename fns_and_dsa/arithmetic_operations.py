def perform_operation (int: num1, int: num2, str: operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose add, substract, multiply divide"





# if __name__ == "__main__":
#     result = perform_operation(10,0,"divide")
#     print(f"Result: {result}")
