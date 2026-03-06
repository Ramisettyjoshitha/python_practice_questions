n=[]
while True:
    num=input("enter the numbers(click q to quit):")
    if num=="q":
        break
    num=int(num)
    n.append(num)
print("duplicate numbers in list:")
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            print(n[i])
            break
