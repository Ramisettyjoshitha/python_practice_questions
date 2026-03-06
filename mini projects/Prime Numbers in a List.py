n=[]
while True:
    num=input("enter numbers for list(enter q to quit):")
    if num=="q":
        break
    num=int(num)
    n.append(num)
print("prime numbers:")
for i in n:
    if i<2:
        continue
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i)

