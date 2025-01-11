FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is the temperature in Celsius or fahrenheit? (C/F)").upper().strip()
        if unit == 'C':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°C is equal to {converted:.2f}°F")
        elif unit == 'F':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°F is equal to {converted:.2f}°C")
        else:
            print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
    except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__": 
    main()