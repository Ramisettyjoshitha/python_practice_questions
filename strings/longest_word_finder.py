s=input("enter text:")
words=s.split()
longest_word=words[0]
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print("longest word is :",longest_word)
        