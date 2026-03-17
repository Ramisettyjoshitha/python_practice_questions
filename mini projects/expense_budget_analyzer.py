expense={}
size=int(input("enter  no of  days you wanna track:"))
for i in range(size):
    day=input("enter the day:")
    amount=int(input("enter amount spent:"))
    expense[day]=amount
total=0
average=0
highest=0
lowest=100000
lowest_day=""
highest_day=""
budget=int(input("Enter your total budget:"))
for day in expense:
    amount=expense[day]
    total+=amount
    if highest<amount:
        highest=amount
        highest_day=day
    if lowest>amount:
        lowest=amount
        lowest_day=day
average=total/len(expense) 
if total>budget:
    status="overspending"
else:
    status="within budget"
print("total expense:",total)
print(f"the highest expense is {highest} on {highest_day}")
print(f"the lowest expense is {lowest} on {lowest_day}")
print("the average is :",average)
print("the budget is:",budget)
print("status:",status)
print("category per day:")
for day in expense:
    amount=expense[day]
    if amount<100:
        category="low"
    elif amount<=300:
        category="medium"
    else:
        category="high"
    print(day,"->",category)
expense={}
size=int(input("enter  no of  days you wanna track:"))
for i in range(size):
    day=input("enter the day:")
    amount=int(input("enter amount spent:"))
    expense[day]=amount
total=0
average=0
highest=0
lowest=100000
lowest_day=""
highest_day=""
budget=int(input("Enter your total budget:"))
for day in expense:
    amount=expense[day]
    total+=amount
    if highest<amount:
        highest=amount
        highest_day=day
    if lowest>amount:
        lowest=amount
        lowest_day=day
average=total/len(expense) 
if total>budget:
    status="overspending"
else:
    status="within budget"
print("total expense:",total)
print(f"the highest expense is {highest}on {highest_day}")
print(f"the lowest expense is {lowest} on {lowest_day}")
print("the average is :",average)
print("the budget is:",budget)
print("status:",status)
print("category per day:")
for day in expense:
    amount=expense[day]
    if amount<100:
        category="low"
    elif 101<amount<=300:
        category="medium"
    else:
        category="high"
    print(day,"->",category)
print("High spending days (above average):")

for day in expense:
    if expense[day] > average:
        print(day, "->", expense[day])