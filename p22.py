#Program to check salary bonus based on years of salary
salary = float(input("Enter your current monthly salary :"))
years = float(input("Enetr your total years of services :"))
if years < 0 or salary < 0:
    print("Invalid data entered ")
    bonus_percent = 0
elif years > 10:
    bonus_percent = 20
elif years >= 5:
    bonus_percent = 10
elif years >= 1:
    bonus_percent = 5
else:
    bonus_percent = 0
bonus_amount = (bonus_percent/100)*salary
total_salary = salary + bonus_amount
if years >= 0 and salary >= 0:
    print(f"\nbonus percentage :{bonus_percent} %")
    print(f"bonus amount : ${bonus_amount} ")
    print(f"Total salary : ${total_salary} ")
