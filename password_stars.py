minimum_length = int(input("Password minimum length: "))
password = input("Password: ")
while len(password) < minimum_length:
    print(f"Password needs to be at least {minimum_length} characters long")
    password = input("Password: ")
print("*" * len(password))
