expense={}
size=int(input("enter number of days:"))
for i in range(size):
    day=input("enter day name:")
    amount=int(input("enter amount:"))
    expense[day]=amount
total=0
highest=0
lowest=100000
average=0
highest_day=""
lowest_day=""
for day in expense:
    amount=expense[day]
    total+=amount
    if amount>highest:
        highest=amount
        highest_day=day
    if amount<lowest:
        lowest=amount
        lowest_day=day
average=total/len(expense)
print("total expense:",total)
print(f"the highest expense is {highest}on {highest_day}")
print(f"the lowest expense is {lowest} on {lowest_day}")
print("the average is :",average)