"""
Write a Python program that:

Asks the user to enter a number

Asks how many multiples they want

Prints the multiplication table of that number

Example:

Enter number: 7
Enter range: 5

Output:

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
"""
n=int(input("enter the number :"))
i=int(input("enter the  range of multiples you want:"))
a=1
while a<=i:
    print(f"{n}*{a}={n*a}")
    a+=1
