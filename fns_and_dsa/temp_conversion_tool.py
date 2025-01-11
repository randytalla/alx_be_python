from datetime import datetime, timedelta

def calculate_future_date():
    """Calculate the future date after adding the specified number of days to the current date."""
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        return future_date.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

# Main block
if __name__ == "__main__":
    future_date = calculate_future_date()
    if future_date:
        print(f"The future date is {future_date}")
