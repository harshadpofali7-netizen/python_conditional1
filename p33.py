# Program to check loan eligibility

age = int(input("Enter your age: "))
income = float(input("Enter your monthly income (₹): "))
credit_score = int(input("Enter your credit score: "))

if age >= 21:    
    if income >= 25000:   
        if credit_score >= 650:   
            print("✅ You are eligible to apply for a loan.")
        else:
            print("❌ Not eligible: Credit score must be at least 650.")
    else:
        print("❌ Not eligible: Monthly income must be at least ₹25,000.")
else:
    print("❌ Not eligible: Age must be at least 21 years.")