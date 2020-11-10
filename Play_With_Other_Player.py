from Singelton import *
from tkinter import *
from TicTacBoard import *

class Play_With_Other_Player:
    def __init__(self):
        self.moves = []

    def openNewWindows(self):
        government = Singleton()

        if not government.openNewWindow:
            gameWindow = Tk()
            gameWindow.title("Tic Tac Toe")
            TicTacBoard(gameWindow)
            gameWindow.mainloop()
