#Program to check whether a number is divisible by 3 and 7 or not
num = int(input("Enter the number :"))
if num % 3 == 0 and num % 7 == 0:
    print(f"{num} is divisible by both 3 and 7")
else:
    print(f"{num} is not divisible by both 3 and 7")
