from turtle import *

def draw_square(length, color1):
    speed(0)
    color(color1,'white')
    begin_fill()
    for i in range(4):
        forward(length)
        left(90)
    end_fill()

draw_square(100, 'red')

mainloop()
