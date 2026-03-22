def num(n):
    fact=1
    while n>0:
        fact=fact*n
        n-=1
    return fact
print(num(4))
