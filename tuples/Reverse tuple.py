t=(1,2,3)
rev=()
for i in t:
    rev=(i,)+rev
print(rev)