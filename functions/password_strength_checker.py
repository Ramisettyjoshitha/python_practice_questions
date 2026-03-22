def password_checker(n):
    special_characters="@#$&"
    has_digit=False
    has_upper=False
    has_special=False
    if " " in n:
        return "invalid password"
    for char in n:
        if char.isdigit():
            has_digit=True
        elif char.isupper():
            has_upper=True
        elif char in special_characters:
            has_special=True
    if len(n)>=8 and has_digit and has_upper and has_special:
        return "strong password"
    if len(n)>= 6 and (has_digit or has_upper):
        return"medium password"
    else:
        return"weak password"
print(password_checker("Joshitha@1"))   
    