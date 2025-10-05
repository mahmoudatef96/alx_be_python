import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    print(f"Current date and time: {current_date}")
    numberof_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.datetime(days = numberof_days)
    print(f"Future date: {future_date}")
