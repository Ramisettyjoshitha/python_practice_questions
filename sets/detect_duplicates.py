l=[1,2,3,2,4,5,1]
s=set()
duplicates=set()
for i in l:
    if i in s:
        duplicates.add(i)
    else:
        s.add(i)
print(duplicates)