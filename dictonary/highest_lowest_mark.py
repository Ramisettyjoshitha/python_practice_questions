student={}
highest=0
lowest=100
highest_student=""
lowest_student=""
size=int(input('enter number of students  data you wanna add:'))
for i in range(size):
    name=input("enter the students name:")
    mark=int(input("enter the marks the student got for 100:"))
    student[name]=mark
    if mark>highest:
        highest=mark
        highest_student=name
    if mark<lowest:
        lowest=mark
        lowest_student=name
print(student)
print(f"the lowest mark is :{lowest} for {lowest_student}")
print(f"the highest mark is :{highest} for {highest_student}")  