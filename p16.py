#Program to find the greatest of three number
num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))
num3 = float(input("Enter the third number"))
if num1 >= num2 and num1 >= num3 :
    greater = num1
elif num2 >= num1 and num2 >= num3:
    greater = num2
else:
    greater = num3
print(f"the greater number is : {greater}")
