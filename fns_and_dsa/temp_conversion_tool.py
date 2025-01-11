FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * FAHRENHEIT_TO_CELSIUS_FACTOR) + 32

def get_user_input():
    while True:
        try:
            user_input = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature Celsius or Fehrenheit? (C/F): ").strip().upper()
            if unit not in ['C', 'F']:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fehrenheit")
                continue
            return user_input, unit
        except ValueError:
                print("Invalid temperature. Please enter a numeric value")

def main():
    user_input, unit = get_user_input()
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(user_input)
        print(f"{user_input}°C is equal to {converted_temp}")
    else:
        converted_temp = convert_to_celsius(user_input)
        print(f"{user_input}°F is equal to {converted_temp}")
        

if __name__ == "__main__": 
    main()


