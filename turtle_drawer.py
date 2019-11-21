import my_enums
from tigr import AbstractDrawer
import turtle
from tkinter import *


class DrawerTurtle(AbstractDrawer):
    def __init__(self, set_width=1000, set_height=1000):
        self.window = Tk()
        canvas = Canvas(self.window, width=set_width, height=set_height)
        canvas.pack()
        self.cursor = turtle.RawPen(canvas)
        self.cursor.speed(1)

    # pen_num should be int
    def select_pen(self, pen_num):
        self.cursor.color(my_enums.Pen.colours[pen_num])

    def pen_down(self):
        self.cursor.pendown()

    def pen_up(self):
        self.cursor.penup()

    # along should be int
    def go_along(self, along):
        self.pen_up()
        self.cursor.setx(along)

    # down should be int
    def go_down(self, down):
        self.pen_up()
        self.cursor.sety(down)

    # direction and distance should be int
    def draw_line(self, direction, distance):
        self.cursor.setheading(direction)
        self.cursor.forward(distance)

    def update(self):
        self.window.mainloop()
