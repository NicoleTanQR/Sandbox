MINIMUM_LENGTH = 7
password = input("Password: ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password needs to be at least {MINIMUM_LENGTH} characters long")
    password = input("Password: ")
print("*" * len(password))
