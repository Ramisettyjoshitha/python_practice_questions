products={}
size=int(input("enter no of products you wonna store:"))
for i in range(size):
    name=input('enter product name:')
    price=int(input('enter product price:'))
    products[name]=price
total=0
for price in products:
    total+=products[price]
print("the total cost of products is :",total)

