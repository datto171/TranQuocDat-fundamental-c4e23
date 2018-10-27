password = input("Input your Password :")

while (len(password) <= 8) or password.isalpha() or \
    (password.isupper() or password.islower() or password.isdigit()):
    print("not Ok")
    if(len(password) <= 8):
        print("password must be greater than 8 character")
    elif password.isalpha():
        print("password must contain number")
    elif (password.isupper() or password.islower or password.isdigit()):
        print("password must be contain both of upper character and lower character")
    else:
        break
    password = input("Input your Password :")

# while (len(password) <= 8) or password.isalpha() or \
#     (password.isupper() or password.islower() or password.isdigit()):

#     print("not Ok")
#     if(len(password) <= 8):
#         print("password must be greater than 8 character")
#     if password.isalpha():
#         print("password must contain number")
#     if (password.isupper() or password.islower or password.isdigit()):
#         print("password must be contain both of upper character and lower character")
#     password = input("Input your Password :")

