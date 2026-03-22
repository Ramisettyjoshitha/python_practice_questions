n=input("enter the sentence:")
def func(n):
    word=n.split()
    longest=word[0]
    for i in word:
        if len(i)>len(longest):
            longest=i
    return f"the longest word is {longest}"
print(func(n))
    
