#Program to calculate discount based on total shopping amount
def calculate_discount(amount):
    if amount >= 5000:
        discount_rate = 0.20   
    elif amount >= 3000:
        discount_rate = 0.15   
    elif amount >= 1000:
        discount_rate = 0.10   
    else:
        discount_rate = 0.05   

    discount = amount * discount_rate
    final_amount = amount - discount
    return discount, final_amount

shopping_amount = float(input("Enter your total shopping amount: ₹"))

discount, final_amount = calculate_discount(shopping_amount)

print(f"Discount applied: ₹{discount:.2f}")
print(f"Final amount to be paid: ₹{final_amount:.2f}")