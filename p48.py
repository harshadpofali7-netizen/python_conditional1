# Program to print language choice using match-case

print(" Language Menu")
print("1. English")
print("2. Hindi")
print("3. Marathi")
print("4. Spanish")
print("5. French")

choice = int(input("Enter your choice (1-5): "))

match choice:
    case 1:
        print("You selected English.")
    case 2:
        print("आपने हिंदी चुनी है।")
    case 3:
        print("तुम्ही मराठी निवडली आहे.")
    case 4:
        print("Has elegido Español.")
    case 5:
        print("Vous avez choisi le Français.")
    case _:
        print("❌ Invalid choice! Please select between 1 and 5.")