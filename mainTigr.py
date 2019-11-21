from tkinter_drawer import DrawerTkinter
from turtle_drawer import DrawerTurtle
from drawer_py_game import DrawerPy
from passer import Parser
from tigr import AbstractSourceReader
from builder_pattern import *


class MainTIGr(AbstractSourceReader):
    def __init__(self, parser):
        super().__init__(parser)

    def go(self):
        self.source = Director(BuildSquare()).write()
        self.parser.parse(self.source)
        # self.source = Director(BuildRectangle()).write()
        # self.parser.parse(self.source)


if __name__ == '__main__':
    main = MainTIGr(Parser(DrawerTurtle()))
    main.go()
    main.parser.drawer.update()
