s=input("enter text :").lower()
vowels="aeiou"
v=0
c=0
for i in s:
    if i in vowels:
        v+=1
    elif i.isalpha():
        c+=1
print("total vowels are:",v)
print("total consonents are:",c)
