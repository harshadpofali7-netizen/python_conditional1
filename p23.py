#Program to calculate electric bill on units consumed
units = float(input("Enetr the total units consumed :"))
total_bill = 0.0
fixed_charge = 50.0
if units < 0:
    print("Invalid units input")
else:
    if units <= 100:
        total_bill = units * 3,5
    elif units <= 300:
        total_bill = (100 * 3.5) + ((units - 100) * 5.00)
    else :
        total_bill = (100 * 3.5) + (200 * 5) + ((units - 300) * 8.00)
    final_amount = total_bill + fixed_charge
    print("\n-----electricity bill summary------")
    print(f"units consumed : {units} units ")
    print(f"energy charges : ${total_bill}")
    print(f"fixed services : ${fixed_charge}")
    