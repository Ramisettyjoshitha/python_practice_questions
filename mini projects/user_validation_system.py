username=input("enter username:")
password=input('enter password:')
email=input("enter email:")
if len(username)>=8 and not "  ":
    print("username valid")
else:
    print("username invalid")
is_number=False
is_special_character=False
for i in password:
    if i.isdigit():
        is_number=True
    if not i.isalnum():
        is_special_character=True
if len(password)>=8 and is_number and is_special_character:
    print("strong password")
else:
    print("weak password")
if "@" in email and "." in email and "  " not in email:
    print("valid email")
else:
    print('invalid email')
