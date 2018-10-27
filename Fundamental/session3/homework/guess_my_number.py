print("101 to quit")
x = input("Guess my number (1-100)? ")
while True:
    if (not x.isdigit()):
        print("Please input number")
        x = input("Guess my number (1-100)? ")
    elif int(x) == 101:
        print("My guess number : 51")
        break
    elif int(x) <= 50:
        print("Too small :(")
        x = input("Guess my number (1-100)? ")
    elif int(x) >= 52:
        print("A liitle too large :(")
        x = input("Guess my number (1-100)? ")
    else:
        print("Bingo")
        break