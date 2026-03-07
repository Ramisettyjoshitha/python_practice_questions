""""
Write a Python program that:

Asks the user for username

Asks the user for password

Allows only 3 attempts

If login is correct → print Login Successful

If login fails 3 times → print Account Locked

Correct credentials:

username = admin
password = 1234
"""
correct_username="admin"
correct_password="1234"
attempts=0
while attempts<=3:
    username=input("enter username:")
    password=input("enter password:")
    attempts+=1
    if username==correct_username and password==correct_password:
        print("login successful")
    else:
        print("login failure")
if attempts>3:
    print("account locked")




