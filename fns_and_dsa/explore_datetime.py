from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.datetime.now()
    current_date = datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")
def calculate_future_date ():
    Future_date = datetime
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.date() + timedelta(days=number_of_days)
    future_date = Future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {future_date}")
