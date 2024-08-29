import calendar

def count_sundays_and_second_saturday(year, month):
    """Count the number of Sundays and find the second Saturday on or before the 14th of the month."""
    sundays = 0
    second_saturday = None
    saturday_count = 0
    
    # Iterate over the days of the month
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        weekday = calendar.weekday(year, month, day)
        
        if weekday == calendar.SUNDAY:
            sundays += 1
        elif weekday == calendar.SATURDAY:
            if day <= 14:
                saturday_count += 1
                if saturday_count == 2:
                    second_saturday = day
                    
    return sundays, second_saturday

def display_month_calendar():
    """Display the calendar for a given month and year with additional features."""
    
    while True:  # Loop until a valid year is provided
        try:
            year = int(input('Enter the year (e.g., 2024): '))
            if year > 0:
                break  # Exit loop if input is a positive integer
            else:
                print("Invalid input! Year must be a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid year.")
            
    while True:  # Loop until a valid month is provided
        try:
            month = int(input('Enter the month (1-12): '))
            if 1 <= month <= 12:
                break  # Exit loop if input is within the valid range
            else:
                print("Invalid input! Please enter a month between 1 and 12.")
        except ValueError:
            print("Invalid input! Please enter a valid month (1-12).")
    
    # Display the calendar for the specified month and year
    print('\nHere is the calendar for your selected month:\n')
    print(calendar.month(year, month))
    
    # Count Sundays and find the second Saturday on or before the 14th
    print('\t*** Number of Holidays in your selected month ***\n')
    sundays, second_saturday = count_sundays_and_second_saturday(year, month)
    print(f"Number of Sundays: {sundays}")
    
    if second_saturday:
        print(f"Second Saturday falls on: {second_saturday} {calendar.month_name[month]} {year}")
    
    # Check if December is selected and highlight December 25
    if month == 12:
        print("\n*** December 25 is Christmas Day! ***\n")
        print(f"\nIt's Christmas Eve, and there’s no place like home!\n\t~~~ Merry Christmas to you! ~~~")
    
    print('\n*** Thank you for using the PK Calendar Program ***\n')

# Call the function
display_month_calendar()
