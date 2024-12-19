# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
i = 0

# While loop to iterate through each row
while i < size:
    # For loop to print asterisks in each row
    for j in range(size):
        print("*", end="")
    # Print a newline character to move to the next row
    print()
    # Increment row counter
    i += 1
