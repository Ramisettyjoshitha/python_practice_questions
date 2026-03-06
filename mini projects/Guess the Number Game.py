"""
Guess the Number Game

Program should:

Computer chooses a number between 1 and 10

User keeps guessing

Program tells:

Too high
Too low
Correct!

Count how many attempts the user took.

Example:

Guess number: 5
Too low

Guess number: 8
Too high

Guess number: 7
Correct! Attempts: 3
"""
secret_number=7
attempts=0

while True:
    n=int(input("enter the number between 1 to 10:"))
    attempts+=1
    if n>secret_number:
        print("guess is tooo high")
    elif n<secret_number:
        print("guess is too low")
    else:
        print("guess is correct")
        print("correct!attempts:",attempts)
        break
