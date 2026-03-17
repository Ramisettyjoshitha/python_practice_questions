contacts=[]
total=0
size=int(input("number of contacts to enter:"))
for i in range(size):
    name=input("enter the contact name :")
    contacts.append[i]
unique_contacts=set(contacts)
seen=set()
duplicates=set()
for name in contacts:
    if name in seen:
        duplicates.add(name)
    else:
        seen.add(name)
print(len(contacts))
print(len(unique_contacts))
print(len(duplicates))
search=input('enter name to serach:')
if search in unique_contacts:
    print('found')
else:
    print("not found")
