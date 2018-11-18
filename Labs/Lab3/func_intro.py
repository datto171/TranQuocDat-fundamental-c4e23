from random import randint, choice
# op_list = ["+", "-", "*", "/"]
# op = choice(op_list)
# error = randint(-1,1)
# a = randint(0, 10)
# b = randint(0,10)

def eval(a, b, op):
    if op == '+':
        r = a + b
    elif op == '-':
        r = a - b
    elif op == '*':
        r = a * b
    elif op == '/':
        r = a / b
    return r

#call function

# s = eval(a, b, op, error)
# print(a, op, b, '=', s[0])
# x = input("Y/N: ")
# if x == 'y':
#     if s[0] == s[1]:
#         print("Chuc mung ban")
#     else:
#         print("Chia buon ban")
# if x == 'n':
#     if s[0] != s[1]:
#         print("Chuc mung ban")
#     else:
#         print("Chia buon ban")