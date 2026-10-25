# Program to build a simple ATM menu using match-case

balance = 10000  

print("🏦 ATM Menu")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

match choice:
    case 1:
        print(f"💰 Your current balance is: {balance}")
    case 2:
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print(f"✅ {deposit} deposited successfully. New balance: {balance}")
    case 3:
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print(f"✅ {withdraw} withdrawn successfully. Remaining balance: {balance}")
        else:
            print("❌ Insufficient balance!")
    case 4:
        print("👋 Thank you for using the ATM. Goodbye!")
    case _:
        print("❌ Invalid choice! Please select between 1 and 4.")