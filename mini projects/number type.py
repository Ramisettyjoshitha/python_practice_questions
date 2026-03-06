a=int(input("enter the number you want to check type:"))
if a==0:
    print("it is neither negative nor positive, it is zero")
elif a>0:
    if a%2 ==0 :
        print('positive even')
    else:
        print("positive odd")
else:
    if a%2 ==0:
        print('negative even')
    else:
        print("negatie odd")
     

