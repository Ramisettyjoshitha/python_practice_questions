expense=[]
total_expense=0
average_expense=0
days=int(input("enter for how many days you want to track your expense:"))
for i in range(days):
    num=int(input(f"enter you day{i+1} of expense:"))
    expense.append(num)
    total_expense=sum(expense)
highest_expense=expense[0]
lowest_expense=expense[0]
highest_day=1
lowest_day=1
for i in range(len(expense)):
    if expense[i]>highest_expense:
        highest_expense=expense[i]
        highest_day=i+1
    if expense[i]<lowest_expense:
        lowest_expense=expense[i]
        lowest_day=i+1
average_expense=total_expense/len(expense)   
print("the total expense is:",total_expense)  
print(f"the lowest expense is {lowest_expense} which is spent on the day{lowest_day}") 
print(f"the highest expense is {highest_expense} which is spent on the day{highest_day}")  
print("the average expense is:",average_expense)  
