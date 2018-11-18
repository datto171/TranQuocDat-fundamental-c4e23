from random import randint, choice
op_list = ["+", "-", "*", "/"]
op = choice(op_list)

x = randint(0,1)

a = randint(0,10)
b = randint(0,10)
error = randint(-1,1)

if x == 0:
    if op == '+':
        print(a, op, b, '=',a+b)
    elif op == '-':
        print(a, op, b, '=',a-b)
    elif op == '*':
        print(a, op, b, '=',a*b)
    elif op == '/':
        if b == 0:
            print("khong the chia cho 0")
        else:
            print(a, op, b, '=',a/b)
            
else:
    if op == '+':
        t = a + b + error
        print(a, op, b, '=',t)
    elif op == '-':
        t = a - b + error
        print(a, op, b, '=',t)
    elif op == '*':
        t = a * b + error
        print(a, op, b, '=',t)
    elif op == '/':
        if b == 0:
            print("khong the chia cho 0")
        else:
            t = a / b + error
            print(a, op, b, '=',t)


