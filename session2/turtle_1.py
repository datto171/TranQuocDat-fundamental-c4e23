from turtle import *

speed(0)
color("red")

for i in range(4):
    if i == 0:
        right(30)
    else:
        right(150) 

    forward(100)
    left(60)
    forward(100)
    left(120)
    forward(100)
    left(60)
    forward(100)

mainloop()