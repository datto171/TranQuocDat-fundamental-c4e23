from random import randint

x = randint(0,100)
print(x)
if x < 30:
    print("Rainy")
elif x < 60:
    print("Cloudy")
else:
    print("Sunny")
