# Program to print weekday name using match-case

day_num = int(input("Enter a number (1-7): "))

match day_num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("❌ Invalid input! Please enter a number between 1 and 7.")