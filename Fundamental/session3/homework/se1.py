user_name = "c4e"
password = "asdfas"
print("Hi there, this is a superuser gateway")
x = input("Username: ")
while True:
    if x == user_name:
        y = input("password: ")
        if y == password:
            print("welcome, c4e")
            break;
        else:
            print("Password is not correct")
    else:
        print("You are not superuser")
        x = input("Username: ")
