n=input("enter the sentence:")
def func(n):
    word=n.split()
    count=0
    for i in word:
        count+=1
    return f"total number of words in sentence {count}"
print(func(n))