# Program to check whether a number lies between 10 and 50

num = int(input("Enter a number: "))

if num > 10:
    if num < 50:
        print("✅ The number lies between 10 and 50.")
    else:
        print("❌ The number does not lie between 10 and 50.")
else:
    print("❌ The number does not lie between 10 and 50.")