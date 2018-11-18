a = int(input("Nhap so a: "))
x = input("Operation (+, -, *, /):")
b = int(input("Nhap so b: "))
if x == '+':
    print(a, x, b, '=',a+b)
elif x == '-':
    print(a, x, b, '=',a-b)
elif x == '*':
    print(a, x, b, '=',a*b)
elif x == '/':
    if b == 0:
        print("khong the chia cho 0")
    else:
        print(a, x, b, '=',a/b)
