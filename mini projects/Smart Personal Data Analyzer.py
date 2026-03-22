def analyze_text(text):
    word=text.split()
    word_count=0
    vowels="aeiou"
    vowel_count=0
    for i in word:
        word_count+=1
    for i in text:
       if i.isalpha():
           if i.lower() in vowels:
                vowel_count+=1
    if len(word)==0:
        return 0,0,"",""
    longest=word[0]
    smallest=word[0]
    for i in word:
        if len(longest)<len(i):
            longest=i
        if len(smallest)>len(i):
            smallest=i
    return word_count,vowel_count,longest,smallest
def analyze_numbers(num):
    total=0
    average=0
    maximum=num[0]
    minimum=num[0]
    for n in num:
        total+=n
    average=total/len(num)
    for n in num:
        if maximum<n:
            maximum=n
        if minimum>n:
            minimum=n
    return total,average,maximum,minimum
def password_checker(password):
    special="@#$&"
    has_digit=False
    has_special=False
    has_upper=False
    if " " in password:
        return"invalid password"
    for char in password:
        if char.isdigit():
            has_digit=True
        elif char.isupper():
            has_upper=True
        elif char in special:
            has_special=True
    if len(password)>=8 and has_digit and has_special and has_upper:
        return "Strong password"
    elif len(password)>=6 and (has_digit or has_upper):
        return 'Medium password'
    else:
        return 'Weak password'
def menu():
    while True:
        print("\n-----smart personal data analyzer-----")
        print("1.text analyzer")
        print("2.number analyzer")
        print("3.password checker")
        print("4.exit")
        choice=int(input("enter choice:"))
        if choice==1:
            text=input("enter sentence:")
            wc,vc,l,s=analyze_text(text)
            print("word count is:",wc)
            print("vowel count:",vc)
            print("longest word is :",l)
            print("smallest word is:",s)
        elif choice==2:
            number=int(input("enter number of numbers you will enter:"))
            num=[]
            for i in range(number):
                value=int(input("enter the number:"))
                num.append(value)
            t,a,m,mi=analyze_numbers(num)
            print("the total is:",t)
            print("the average is:",a)
            print("the maximum number is:",m)
            print("the minimum number is:",mi)
        elif choice==3:
            password=input("enter password:")
            result=password_checker(password)
            print(result)
        elif choice==4:
            print("exiting")
            break
        else:
            print("invalid choice try again")
menu()




    


        

               


