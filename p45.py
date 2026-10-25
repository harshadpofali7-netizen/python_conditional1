# Program to print menu-based food selection using match-case

print(" Food Menu")
print("1. Pizza")
print("2. Burger")
print("3. Pasta")
print("4. Sandwich")
print("5. Salad")

choice = int(input("Enter your choice (1-5): "))

match choice:
    case 1:
        print("You selected  Pizza.")
    case 2:
        print("You selected  Burger.")
    case 3:
        print("You selected  Pasta.")
    case 4:
        print("You selected  Sandwich.")
    case 5:
        print("You selected  Salad.")
    case _:
        print("❌ Invalid choice! Please select between 1 and 5.")