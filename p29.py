# Program to check blood donation eligibility

def check_eligibility(age, weight):
    if age >= 18 and age <= 65:
        if weight >= 50:
            return "✅ You are eligible to donate blood."
        else:
            return "❌ You are not eligible: Minimum weight required is 50 kg."
    else:
        return "❌ You are not eligible: Age must be between 18 and 65 years."

age = int(input("Enter your age: "))
weight = float(input("Enter your weight (in kg): "))

result = check_eligibility(age, weight)
print(result)