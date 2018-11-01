characterlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# x = input("".lower())
x = input("Input your String:").lower()

count = {}
for i in x:
    if i in characterlist:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

for i in characterlist:
    if i in count:
        print(i, count[i], sep=": ")

