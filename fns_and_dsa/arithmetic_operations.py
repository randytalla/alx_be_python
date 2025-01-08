def perform_operation (num1:float, num2:float, operation:str):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero is not allowed"
        case _:
            return "Error: Invalid operation"


if __name__ == "__main__":
    result = perform_operation(10,0,"divide")
    print(f"Result: {result}")
