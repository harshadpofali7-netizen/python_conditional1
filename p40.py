# Program to check whether a password is valid using nested if

password = input("Enter your password: ")

if len(password) >= 8:   
    if any(char.isdigit() for char in password):   
        if any(char in "@#$%" for char in password):   
            print("✅ Password is valid.")
        else:
            print("❌ Password invalid: Must contain at least one special character (@, #, $, %).")
    else:
        print("❌ Password invalid: Must contain at least one digit.")
else:
    print("❌ Password invalid: Must be at least 8 characters long.")