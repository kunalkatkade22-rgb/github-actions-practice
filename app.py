#this code is from google 
import calendar

# Get the year input from the user
year = int(input("Enter a year: "))

# Check using the built-in function
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
