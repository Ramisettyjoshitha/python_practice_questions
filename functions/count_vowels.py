vowels="aeiou"
def func(n):
    count=0
    for i in n:
        if i.isalpha():
            if i.lower() in vowels:
                count+=1
    return count
print(func("apple"))

