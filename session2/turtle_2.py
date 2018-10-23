from turtle import *

speed(0)
n = 150

color("blue")
for i in range(3):
    forward(n)
    left(120)

color("red")
for i in range(4):
    forward(n)
    left(90)

color("blue")
for i in range(5):
    forward(n)
    left(72)

color("red")
for i in range(6):
    forward(n)
    left(60)


mainloop()