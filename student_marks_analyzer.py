"""
📌 Problem
Write a Python program that:
Takes student marks from the user
User can enter marks until they type q to stop
Store all marks in a list
After collecting marks, your program should calculate:
 Total number of students
 Highest mark
 Lowest mark
 Average mark
 Number of students who passed
(Pass if mark ≥ 40)
 Number of students who failed
(Fail if mark < 40)
Example Input
Enter mark: 78
Enter mark: 45
Enter mark: 90
Enter mark: 60
Enter mark: 33
Enter mark: q
List becomes
[78, 45, 90, 60, 33]
Expected Output
Total students: 5
Highest mark: 90
Lowest mark: 33
Average mark: 61.2
Passed students: 4
Failed students: 1
"""
marks=[]
total_mark=0
average_mark=0
students_pass=0
students_fail=0
size=int(input("enter the number of marks you are going to enter:"))
for i in range(size):
    mark=int(input("enter students marks:"))
    marks.append(mark)
    total_mark+=mark
lowest_mark=marks[0]
highest_mark=marks[0]
for i in marks:
    if i>highest_mark:
        highest_mark=i
    if i<lowest_mark:
        lowest_mark=i
    if i>=40:
        students_pass+=1
    else:
        students_fail+=1
average_mark=total_mark/len(marks)
print("the total students is:",len(marks))
print("highest mark is :",highest_mark)
print("lowest mark is:",lowest_mark)
print("average mark is:",average_mark)
print("students passed:",students_pass)
print("students failed:",students_fail)


