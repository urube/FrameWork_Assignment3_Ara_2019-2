from abc import ABCMeta, abstractmethod


class AbstractBuilder(metaclass=ABCMeta):

    def __init__(self):
        self.source = ''

    def get_result(self):
        return self.source

    @abstractmethod
    def select_pen(self):
        pass

    @abstractmethod
    def go_up(self):
        pass

    @abstractmethod
    def go_right(self):
        pass

    @abstractmethod
    def go_down(self):
        pass

    @abstractmethod
    def go_left(self):
        pass


class BuildRectangle(AbstractBuilder):

    def select_pen(self):
        self.source += 'P 2'

    def go_up(self):
        self.source += '\nN 200'

    def go_right(self):
        self.source += '\nE 100'

    def go_down(self):
        self.source += '\nS  200'

    def go_left(self):
        self.source += '\nW 100'


class BuildSquare(AbstractBuilder):

    def select_pen(self):
        self.source += 'P 2 # select pen 2'

    def go_up(self):
        self.source += '\nE 100'

    def go_right(self):
        self.source += '\nS 100'

    def go_down(self):
        self.source += '\nW 100'

    def go_left(self):
        self.source += '\nN 100'


class Director(object):

    def __init__(self, builder):
        self.builder = builder

    def write(self):
        self.builder.select_pen()
        self.builder.go_up()
        self.builder.go_right()
        self.builder.go_down()
        self.builder.go_left()
        return self.builder.get_result()
