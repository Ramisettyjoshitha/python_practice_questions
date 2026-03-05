n=int(input("enter number:"))
i=2
is_prime=True
while n>i:
    if n%i==0:
        is_prime=False
        break
    i+=1
if is_prime and n>1:
    print("prime number")
else:
    print("not prime")