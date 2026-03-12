word=input('enter the word:')
freq={}
for char in word:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)