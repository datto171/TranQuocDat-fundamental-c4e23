# items = [] #empty list
# print(items)
# print(type(items))

items = ["Mi", "Pho", "Com rang"]
len(items)
for i in range(len(items)):
    print(i+1, items[i])
# print(*items,sep=", ")

# Update
# k = int(input("Position you want to update? : "))
# new_value = input("You will replacing ?: ")
# items[k-1] = new_value
# print(*items,sep=", ")

# Delete
k = int(input("Position you want to delete? : "))
items.pop(k-1)
for i in range(len(items)):
    print(i+1, items[i])

# items.pop(1)
# print(items)
# items.remove("Pho")
# print(items)