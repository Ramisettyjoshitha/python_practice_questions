s=input("enter text:")
result=""
for i in s:
    if i not in result:
        result+=i
print(result)