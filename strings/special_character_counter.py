s=input('enter text:')
count=0
for i in s:
    if  not i.isalpha() and s !="":
        count+=1
print("total number of special characters:",count)