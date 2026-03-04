n=int(input("enter the number:"))
sum=0
product=1
while n>0:
    digit=n%10
    sum+=digit
    product*=digit
    n //=10
print("sum of digits:",sum)
print("product of digits:",product)
