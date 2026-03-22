def email_validator(email):
    if "@" in email and "." in email and " " not in email:
        return "valid email"
    else:
        return "invalid email"
print(email_validator("joshitha@gmail.com"))