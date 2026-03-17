t=(1,2,3,3,4,4,7,8,7,3)
new=()
for i in t:
    if i not in new:
        new+=(i,)
print(new)
