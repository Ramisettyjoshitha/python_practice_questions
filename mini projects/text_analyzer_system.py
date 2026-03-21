n=input("enter the sentence:").strip()
word=n.split()
count_words=0
count=0
vowels="aeiou"
vowel=0
cons=0
freq={}
result=""
characters=""
characters_count=0
for char in word:
    count_words+=1
for char in word:
    for i in char:
        count+=1
for i in n:
    if i.isalpha():
        if i.lower() in vowels:
           vowel+=1
        else:
            cons+=1
for i in word:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("word frequency:")
for i in freq:
    print(i,"->",freq[i])
longest=word[0]
smallest=word[0]
for i in word:
    if len(i)>len(longest):
        longest=i
    if len(i)<len(smallest):
        smallest=i
reverse=n[::-1]
for i in word:
    if i not in result:
        result+=i+" "
for i in n:
    if not i.isalnum() and i !=" ":
        characters+=i
        characters_count+=1    
print("no of words in sentence:",count_words)
print("no of letters in words:",count)
print("no of vowels:",vowel)
print("no of consonents:",cons)
print("longest word:",longest)
print("smallest word:",smallest)
print("reversed sentence:",reverse)
print("sentence after duplication:",result)
print(" total no of special characters:",characters_count)
if characters_count==0:
    print("no special characters to print")
else:
    print("special characters list:",characters)   

        









    
