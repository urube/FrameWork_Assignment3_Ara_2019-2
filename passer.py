from tigr import AbstractParser, AbstractSourceReader
import re


class Parser(AbstractParser):

    def __init__(self, drawer):
        super().__init__(drawer)
        self.command_list = {
            "P": "self.drawer.select_pen(self.data)",
            "D": "self.drawer.pen_down()",
            "N": "self.drawer.draw_line(0, self.data)",
            "E": "self.drawer.draw_line(90, self.data)",
            "S": "self.drawer.draw_line(180, self.data)",
            "W": "self.drawer.draw_line(270, self.data)",
            "X": "self.drawer.go_along(self.data)",
            "Y": "self.drawer.go_down(self.data)",
            "U": "self.drawer.pen_up()"
        }

    def parse(self, raw_source):
        self.source = raw_source.splitlines()
        for line in self.source:
            inputs = re.findall("\w+", line)
            self.data = re.findall("\d+", line)
            self.command = inputs[0].upper()
            if len(self.data) > 0:
                self.data = int(float(self.data[0]))
            try:
                parsed_command = self.command_list[self.command[0]]
                exec(parsed_command)
            except ValueError as e:
                print(f'{e}: Value outside boundary')
            except KeyError as e:
                print(f'{e}: Not a command')
