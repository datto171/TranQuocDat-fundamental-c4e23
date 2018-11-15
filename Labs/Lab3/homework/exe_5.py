from turtle import *

def draw_star(x, y, length):
    penup()
    setpos(x, y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)

draw_star(150,150,100)
mainloop()