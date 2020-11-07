
print("Welcome to JExpress Bank!")
print("Welcome to the withdrawal service.")
print("Your account balance remains 5000")

withdrawal_amt = 0
Saving_amt = 5000

while withdrawal_amt != 5000:
    withdrawal_amt = int(input("Amount to be withdrawn: "))

    if Saving_amt >= withdrawal_amt:
        total_bal = Saving_amt - withdrawal_amt
        print("Your balance remains", total_bal, "naira")
        Saving_amt = total_bal
    else:
        print("Insufficient balance")
        print("You will need to make more deposit or get a loan from the bank. Thank you!")