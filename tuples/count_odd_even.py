t=(1,2,3,4,5,6,7,8,9,10)
even=0
odd=0
for i in t:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("total even:",even)
print("total odd:",odd)