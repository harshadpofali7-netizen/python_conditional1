# Program to check user role using match-case

role = input("Enter your role (admin/user/guest): ").lower()

match role:
    case "admin":
        print(" Welcome Admin! You have full access.")
    case "user":
        print(" Welcome User! You have limited access.")
    case "guest":
        print(" Welcome Guest! You have view-only access.")
    case _:
        print(" Invalid role! Please enter admin, user, or guest.")