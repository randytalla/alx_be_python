import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return print (f"The current date and time is {formatted_date}")

def calculate_future_date(days: int):
    current_date = datetime.datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date.strftime("%Y-%m-%d")




display_current_datetime()
days = int(input("Enter the number of days to add the current date: "))

future_date = calculate_future_date(days)
print(f"Future date is {future_date}")