# Program to check whether a number is greater than 0 and less than 100

num = int(input("Enter a number: "))

if num > 0:   
    if num < 100:   
        print("✅ The number lies between 0 and 100.")
    else:
        print("❌ The number is greater than or equal to 100.")
else:
    print("❌ The number is less than or equal to 0.")