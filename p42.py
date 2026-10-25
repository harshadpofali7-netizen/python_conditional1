# Program to perform calculator operations using match-case

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose operation: +, -, *, /")

operation = input("Enter your choice: ")

match operation:
    case "+":
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("❌ Error: Division by zero is not allowed.")
    case _:
        print("❌ Invalid operation! Please choose +, -, *, /")