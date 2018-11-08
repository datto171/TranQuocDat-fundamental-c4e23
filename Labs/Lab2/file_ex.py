content = "van ban quy"
#Cach 1
# write
# with open("content.txt", "w") as f:
#     f.write(content)

#read
with open("content.txt", "r") as f:
    c = f.read()
    print(c)

#Cach 2
#1. open file - #2. ghi file - #3. dong file
# f = open("content.txt", "w")    # write
# f.write(content)
# f.close()