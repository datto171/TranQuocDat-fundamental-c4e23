n = int(input("Nhap n = "))
for i in range(n):
    if i % 2 != 0:
        j = "* "
    else:
        j = "x "
    
    print(j,end='')