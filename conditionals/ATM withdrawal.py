#ATM withdrawal.
a=int(input("enter your current bank balance:"))
b=int(input("enter your withdrawal amount:"))
if a>b:
    current_balance=a-b
    print("withdrawal is successfull")
    print("you current balance after withdrawal:",current_balance)
else:
    print('withdrwal is unsucessfull as current bank balance is less than withdrawal amount')