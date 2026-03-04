correct_password="python123"
attempts=3
while attempts>0:
    password=input("enter password:")
    if password == correct_password:
        print("access granted")
        break
    else:
        attempts -= 1
        print("wrong password try again,attempts left:",attempts)
if attempts == 0:
    print("Account Locked")

    