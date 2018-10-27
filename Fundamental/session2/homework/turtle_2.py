from turtle import *

speed(0)
n = 150
for i in range(3,7):
    if i % 2 == 0:
        color("red")
    else:
        color("blue")

    for x in range(i):
        forward(n)
        left(360/i)

mainloop()