# Program to check driving license eligibility

age = int(input("Enter your age: "))
test_passed = input("Have you passed the driving test? (yes/no): ").lower()

if age >= 18:   
    if test_passed == "yes":  
        print("✅ You are eligible to apply for a driving license.")
    else:
        print("❌ You are not eligible: Driving test not passed.")
else:
    print("❌ You are not eligible: Age must be at least 18 years.")