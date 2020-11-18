from Singelton import *
from tkinter import *
from TicTacBoard import *
from tkinter import messagebox


class WindowsHandler:
    def __init__(self):
        self.moves = []
        self.government = None
        self.gameWindow = None

    # def on_closing(self):
    #     if messagebox.askokcancel("Quit", "Do you want to quit?"):
    #         print("exit window")
    #         self.government = None
    #         self.gameWindow.destroy()

    def openNewWindow(self, game_mode):
        self.government = Singleton()

        if not self.government.openNewWindow:
            self.gameWindow = Tk()
            self.gameWindow.title("Tic Tac Toe")
            TicTacBoard(self.gameWindow, game_mode)
            # self.on_closing()
            # self.gameWindow.protocol("WM_DELETE_WINDOW", on_closing)
            self.gameWindow.mainloop()

