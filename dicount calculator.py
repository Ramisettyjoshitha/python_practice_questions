# dicount calculator
amount=int(input("enter the total bill:"))
if amount >= 5000:
    discount=amount*0.2
elif amount >= 10000:
    discount=amount*0.5
else:
    discount=amount*0.1
total_bill=amount-discount
print("the final amount is :",total_bill)