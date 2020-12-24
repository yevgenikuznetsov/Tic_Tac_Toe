from enum import Enum

class Mark(Enum):
    X = 2
    O = 4
    EMPTY = 8

class TicTacButton:
    def __init__(self, button, mark):
        """ 
        The constructor for TicTacButton class.     
        
         Parameters: 
         button (Button): cell of the tic-tac-toe game board 
         mark (Mark):  X, O or empty
        """
        self.button = button
        self.mark = mark
