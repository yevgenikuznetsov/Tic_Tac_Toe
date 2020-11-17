from Singelton import *
from tkinter import *
from TicTacBoard import *
from tkinter import messagebox

class WindowsHandler:
    def __init__(self):
        self.moves = []
        self.government = None

    def openNewWindow(self, game_mode):
        self.government = Singleton()

        if not self.government.openNewWindow:
            gameWindow = Tk()
            gameWindow.title("Tic Tac Toe")
            TicTacBoard(gameWindow, game_mode)
            # if messagebox.askokcancel("Quit", "Do you want to quit?"):
            #     print("exit window")
            #     self.government = None
            gameWindow.mainloop()


