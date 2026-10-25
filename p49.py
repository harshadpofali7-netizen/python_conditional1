# Program to print result status using match-case

marks = int(input("Enter your marks (0-100): "))

match marks:
    case m if m >= 75:
        print("🎉 Distinction! Excellent performance.")
    case m if m >= 40:
        print("✅ Pass. Keep working hard.")
    case m if m < 40:
        print("❌ Fail. Needs improvement.")
    case _:
        print("Invalid input! Marks must be between 0 and 100.")