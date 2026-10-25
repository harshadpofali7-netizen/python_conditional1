import calendar
#program to check if yera is a leap year
year = int(input("Enter a year:"))
if calendar.isleap(year):
    print(f"{year} is a leap year:")
else:
    print(f"{year} is not a leap year:")
