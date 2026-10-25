# Program to check whether a year is a leap year and century year

year = int(input("Enter a year: "))

if year % 100 == 0:
    print(f"{year} is a Century Year.")
else:
    print(f"{year} is not a Century Year.")

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")