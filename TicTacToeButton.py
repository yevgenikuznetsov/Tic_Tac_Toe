from enum import Enum

class Mark(Enum):
    X = 2
    O = 4
    EMPTY = 8

class TicTacButton:
    def __init__(self, button,mark):
        self.button = button
        self.mark = mark
