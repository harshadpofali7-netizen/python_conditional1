#Program to check month name by there month number
month_number = int(input("Enter a month number (1-12):"))
months = {
    1: "january",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "july",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
        }
if month_number is months:
    print(f"month number {month_number} is **{months[month_number]}**.")
else:
    print("invalid input! please enter number from 1 to 12 :")
