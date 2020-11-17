from tkinter import *
from WindowsHandler import *
ONE_PLAYER_MODE = 1
TWO_PLAYERS_MODE = 2


mainWindow = Tk()
mainWindow.title("Tic Tac Toe")
mainWindow.geometry("468x210+300+100")

mainWindowLabel = Label(mainWindow,font= " none 30 bold", text="Tic Tac Toe", pady= 30, padx=10).grid(row=0, column=0)

windowsHandler = WindowsHandler()

playWithComp = Button(mainWindow, text = "PLAY WITH COMPUTER", padx = 25, pady = 14,command = lambda:  windowsHandler.openNewWindow(ONE_PLAYER_MODE))
playWithOther = Button(mainWindow, text = "PLAY WITH OTHER PLAYER", padx = 25, pady = 14,command =lambda: windowsHandler.openNewWindow(TWO_PLAYERS_MODE))


playWithComp.grid(row=1,column=0, padx=8, pady=10)
playWithOther.grid(row=1,column=1)


mainWindow.mainloop()
