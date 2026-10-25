# Program to print grade description using match-case

grade = input("Enter grade (A, B, C, D, F): ").upper()

match grade:
    case "A":
        print("🌟 Excellent! Outstanding performance.")
    case "B":
        print("👍 Good! Keep up the effort.")
    case "C":
        print("🙂 Average. You can improve.")
    case "D":
        print("⚠️ Below Average. Work harder next time.")
    case "F":
        print("❌ Fail. Needs significant improvement.")
    case _:
        print("Invalid grade! Please enter A, B, C, D, or F.")