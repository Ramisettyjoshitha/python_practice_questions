s=input("enter text:")
words=s.split()
freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
for word in freq:
    print(word,"->",freq[word])