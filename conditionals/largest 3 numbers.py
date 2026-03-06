#largest 3 numbers
a1=int(input("enter number1:"))
a2=int(input("enter number2:"))
a3=int(input("enter number3:"))
if a1>a2 and a1>a3:
    print("largest number is :",a1)
elif a2>a1  and a2>a3:
    print("largest number is:",a2)
else:
    print("largest number is:",a3)