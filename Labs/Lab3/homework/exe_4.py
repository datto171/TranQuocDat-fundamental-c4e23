from turtle import *

def draw_square(length, color):
    speed(0)
    fillcolor(color,'white')
    begin_fill()
    for i in range(4):
        forward(length)
        left(90)
    end_fill()


for i in range(30):
    draw_square(i * 7, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
