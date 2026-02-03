print("enter your account balance")
balance = int(input())
print("enter transaction amount")
transaction_amount = int(input())
print("enter verification status (True/False)")
is_verified = bool(input())
if is_verified and transaction_amount <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
