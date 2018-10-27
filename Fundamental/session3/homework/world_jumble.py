from random import *

list_words = ["champion", "hello", "vegetable", "brave", "banana"]
x  = randint(0,len(list_words)-1)
z = list(list_words[x])
shuffle(z)

print("Input 'stop' to quit")
print(*z,sep=" ")
answer = input("Your answer: ")
while True:
    if answer == "stop":
        print("My answer is :", list_words[x])
        break
    elif answer == list_words[x]:
        print("Hura")
        break
    else:
        print(":(")
        answer = input("Your answer: ")