"""Logic:
Count the number of digits (
).
Extract each digit, raise it to the power of 
, and sum them.
Compare the sum to the original number"""
n=int(input("enter number:"))
total=0
original=n
while n>0:
    digit=n%10
    total+=digit**3
    n//=10
if original == total:
    print("armstrong number")
else:
    print("not an armstrong number")