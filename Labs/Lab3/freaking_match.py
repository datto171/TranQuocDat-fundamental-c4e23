from random import randint, choice
# import func_intro
from func_intro import eval

def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    op_list = ["+", "-", "*", "/"]
    o = choice(op_list)
    error = randint(-1,1)
    r = eval(x, y, o) + error
    return x, y, o, r
a, b, op, r = generate_quiz()
print(a, op, b, '=', r)


# s = func_intro.eval(x, y, op, error)
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

# input("asd").upper()