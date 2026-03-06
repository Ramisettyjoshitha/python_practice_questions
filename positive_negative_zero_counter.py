n=[]
positive=0
negative=0
zero=0

while True:
    num=input("enter numbers for list (q to stop):")
    if num=="q":
        break
    num=int(num)
    n.append(num)
for i in n:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
    else:
        zero+=1
print('the number of positive numbers:',positive)
print('the number of negative numbers:',negative)
print('the number of zeros:',zero)
    
