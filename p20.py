#Program to check ticket price based on age
age = int(input("Enter your age :"))
if age < 0:
    print("Invalid age entered.")
elif age <= 3:
    print("Ticket price : free ")
elif age <= 12:
    print("Ticket price : ₹100 (child)")
elif age <= 60:
    print("Ticket price : ₹200 (adults)")
else:
    print("Ticket price :₹120 (senior)")
    