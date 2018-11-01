# Exercise 1.1 / 1.2 / 1.3 / 1.4 / 1.6
list_size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and these are my sheep size: ")
print(list_size)
x = max(list_size)
print("Now my biggest sheep has size", x, "let's shear it")
list_size[list_size.index(x)] = 8
print("After shearing, here is my flock")
print(list_size)

for i in range(1,4):
    print("MONTH", i, ":")
    print("One month has passed, now here is my flock")
    for j in range(len(list_size)):
        list_size[j] = list_size[j] + 50
    print(list_size)
    if i == 3:
        break
    else:
        x = max(list_size)
        print("Now my biggest sheep has size", x, "let's shear it")
        list_size[list_size.index(x)] = 8
        print("After shearing, here is my flock")
        print(list_size)

print("My flock has size in total: ", sum(list_size))
print("I would like to get", sum(list_size), "* 2", "=", sum(list_size)*2)