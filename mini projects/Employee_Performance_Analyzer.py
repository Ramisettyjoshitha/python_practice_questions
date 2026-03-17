employees=(
 ("Alice", 85, 70000),
 ("Bob", 92, 80000),
 ("Charlie", 60, 50000),
 ("David", 45, 40000)
)
high=employees[0]
low=employees[0]
total_score=0
total_salary=0
average=0
average=0
for i in employees:
    name, score, salary = i
    total_score+=score
    total_salary+=salary
    if score>high[1]:
        high=i
    if score<low[1]:
        low=i
average=total_score/len(employees)
print(f"highest performer : {high[0]} -> {high[1]}")
print(f"lowest performer : {low[0]} -> {low[1]} ")
print("total salary is :",total_salary)
print("total score is :",total_score)
print("average performace of employees:",average)
print("employees grades:")
for i in employees:
    name, score, salary=i
    if score>=90:
        grade="excellent"
    elif score>=75:
        grade="good"
    elif score>=50:
        grade="average"
    else:
        grade="poor"
    print(name,"->",grade)
print(" below average performers:")
for i in employees:
    name, score, salary = i
    if score<average:
        print(name)






