
print("Welcome to JExpress Bank!")
print("Welcome to the withdrawal service.")
print("Your account balance remains 5000")

Saving_amt = 5000

withdrawal_amt = int(input("Amount to be withdrawn: "))

if Saving_amt > withdrawal_amt:
    total_bal = Saving_amt - withdrawal_amt
    print("Your balance remains", total_bal,"naira")
    print("Do rate our service. Thank you!")
else:
    print("Insufficient Balance!")
    print("If you are in need of a loan, call the customer care service.")
