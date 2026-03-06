"""
Given a list of numbers, print:

Total numbers

Even numbers

Odd numbers

Sum of even numbers

Sum of odd numbers

Example list

[4, 7, 10, 3, 6]

Output

Total numbers: 5
Even numbers: 3
Odd numbers: 2
Sum of even numbers: 20
Sum of odd numbers: 10

"""
n=[]
even=0
odd=0
total=0
sum_even=0
sum_odd=0
size=int(input("enter the numbers you would like to enter in list:"))
for i in range(size):
    num=int(input(f"enter {size} numbers for list:"))
    n.append(num)
for i in n:
    if i%2==0:
         even+=1
         sum_even+=i  
    else:
        odd+=1
        sum_odd+=i
total=len(n)
print("total numbers is :",total)
print("total even numbers is :",even)
print("total odd numbers is :",odd)
print("total  sum of even numbers is :",sum_even)
print("total  sum of odd numbers is :",sum_odd)


    
    
