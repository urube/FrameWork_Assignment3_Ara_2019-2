import my_enums
from tigr import AbstractDrawer
from tkinter import *


class DrawerTkinter(AbstractDrawer):

    def __init__(self, set_width=1000, set_height=1000):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=set_width, height=set_height)
        self.canvas.grid(row=0, column=0)
        self.colour = ''
        self.src_x = 500
        self.src_y = 500
        self.des_x = 0
        self.des_y = 0
        self.penIsDown = False

    def select_pen(self, pen_num):
        self.colour = my_enums.Pen.colours[pen_num]
        print("Current colour is " + self.colour)

    def pen_down(self):
        self.penIsDown = True
        print("penIsDown == " + str(self.penIsDown))

    def pen_up(self):
        self.penIsDown = False
        print("penIsDown == " + str(self.penIsDown))

    def go_along(self, along):
        self.src_x += along
        print("Move " + str(along) + " along")
        print("source_x == " + str(self.src_x) + "source_y == " + str(self.src_y))

    def go_down(self, down):
        self.src_y += down
        print("Move " + str(down) + " along")
        print("source_x == " + str(self.src_x) + "source_y == " + str(self.src_y))

    def draw_line(self, direction, distance):
        if direction == 90:
            self.des_y = self.src_y - distance
            self.des_x = self.src_x
            print("going UP " + str(distance))
        if direction == 270:
            self.des_y = self.src_y + distance
            self.des_x = self.src_x
            print("going DOWN " + str(distance))
        if direction == 0:
            self.des_x = self.src_x + distance
            self.des_y = self.src_y
            print("going RIGHT " + str(distance))
        if direction == 180:
            self.des_x = self.src_x - distance
            self.des_y = self.src_y
            print("going LEFT  " + str(distance))

        if self.penIsDown:
            print("src_x == " + str(self.src_x) + "/ src_y == " + str(self.src_y) + "des_x == " + str(
                self.des_x) + "/ des_y == " + str(self.des_y))
            self.canvas.create_line(self.src_x, self.src_y, self.des_x, self.des_y, fill=self.colour)
            print("just drew a line")

        self.src_x, self.src_y = self.des_x, self.des_y
        print("source_x == " + str(self.src_x) + "source_y == " + str(self.src_y))

    def update(self):
        self.window.mainloop()
