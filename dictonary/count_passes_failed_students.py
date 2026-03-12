students={}
pass_count=0
fail_count=0
pass_students=[]
fail_students=[]
size=int(input("enter number of students data you gonna store and do following operations:"))
for i in range(size):
    name=input('enter student name:')
    mark=int(input('enter student mark:'))
    students[name]=mark
    if mark>=40:
        pass_count+=1
        pass_students.append(name)
    else:
        fail_count+=1
        fail_students.append(name)
print(" total passed students:",pass_count)
print("total failed students:",fail_count)
print("passed students are:",pass_students)
print("failed students:",fail_students)

