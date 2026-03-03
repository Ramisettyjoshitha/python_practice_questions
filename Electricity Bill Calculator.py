#Electricity Bill Calculator
units=int(input("enter the electricity units:"))
if units <= 100:
    bill=units*2
elif units <= 200:
    bill=units*4
else:
    bill=units*6
print("the final bill is :",bill)