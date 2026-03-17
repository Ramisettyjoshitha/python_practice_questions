phonebook={}
size=int(input("enter the number of times you wanna enter data:"))
for i in range(size):
    name=input("enter name:")
    num=int(input("enter phone number:"))
    phonebook[name]=num
search=input("enter the person name whose details you wanna search:")
if search in phonebook:
    print("phone number:",phonebook[search])
else:
    print("not found")
    