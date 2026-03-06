"""
Create a Python program that:

Takes numbers from the user (until user enters 0 to stop)

Stores them in a list

Finds and prints:

Largest number

Smallest number

Sum of numbers

Average of numbers
"""
n=[]
total=0
average=0
while True:
    num=int(input("enter the numbers (enter 0 to stop):"))
    if num==0:
        break
    n.append(num)
largest=n[0]
smallest=n[0]
for i in n:
    total+=i
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
average=total/len(n)
print("the sum of numbers is :",total)
print("the largest is :",largest)
print("the smallest is :",smallest)
print("the average is :",average)

        

    