a = ["Tshirt", "Sweater"]
s = input("Welcome to our shop, what do you want? ")
if s == "R" or s == "r":
    print("Our item :", *a, sep=" ")
elif s == "C" or s == "c":
    x = input("Enter new item: ")
    a.append(x)
    print("Our item : ", *a, sep=" ")
elif s == "U" or s == "u":
    i = int(input("Update position? "))
    new_value = input("New item?")
    a[i-1] = new_value
    print("Our item : ", *a, sep=" ")
elif s == "D" or s == "d":
    i = int(input("Delete position? "))
    a.pop(i-1)
    print("Our item : ", *a, sep=" ")
else:
    print("Ban vui long chi nhap cac gia tri 'C', 'R', 'U', 'D'")
    s = input("Welcome to our shop, what do you want? ")