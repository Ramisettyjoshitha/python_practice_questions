"""Create a program that repeatedly asks the user to enter numbers. 
The program stops when the user enters 0.
 Then it should display:
   Total numbers entered 
   Sum of numbers
     Average
       Count of even numbers
         Count of odd numbers 
         Largest number 
         Smallest number"""
total_numbers=0
sum=0
average=0
count_event=0
count_odd=0
largest=None          #None means no value yet
smallest=None
while True:
    n=int(input('enter the number:'))
    if n==0:
        break
    total_numbers+=1
    sum+=n
    if n%2==0:
        count_event+=1
    else:
        count_odd+=1
    if largest is None or n > largest:
        largest = n
    if smallest is None or n< smallest:
        smallest = n
    if n>0:
        average=sum/total_numbers
    else:
        average=0
print("total numbers is :",total_numbers)
print("sum  is :",sum)
print("average is :",average)
print(" total even numbers is :",count_event)
print("total odd numbers is :",count_odd)
print("the largest is :",largest)
print("the smallest is :",smallest)


    

