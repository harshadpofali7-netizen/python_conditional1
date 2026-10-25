# Program to check the type of number (single, double, or three digit)

def check_number_type(num):
    if -9 <= num <= 9:
        return "Single-digit number"
    elif -99 <= num <= 99:
        return "Double-digit number"
    elif -999 <= num <= 999:
        return "Three-digit number"
    else:
        return "Number has more than three digits"

number = int(input("Enter a number: "))

result = check_number_type(number)
print(result)