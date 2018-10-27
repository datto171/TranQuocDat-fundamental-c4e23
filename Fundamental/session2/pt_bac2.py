a = int(input("Nhap a = "))
b = int(input("Nhap b = "))
c = int(input("Nhap c = "))

x1 = 0
x2 = 0

delta = b*b - 4*a*c
if(delta < 0):
    print("pt vo nghiem")
elif(delta == 0):
    print("pt co 1 nghiem")
    x1 = x2 = (-b)/(2*a)
    print(x1)
else:
    print("pt co 2 nghiem")
    x1 = (-b+delta**0.5)/(2*a)
    x2 = (-b-delta**0.5)/(2*a)
    print(x1)
    print(x2)

