from tkinter import *
from Play_With_Other_Player import *

mainWindow = Tk()
mainWindow.title("Tic Tac Toe")
mainWindow.geometry("468x210+300+100")

mainWindowLabel = Label(mainWindow,font= " none 30 bold", text="Tic Tac Toe", pady= 30, padx=10).grid(row=0, column=0)

playWithOtherPlayer = Play_With_Other_Player()


playWithComp = Button(mainWindow, text = "PLAY WITH COMPUTER", padx = 25, pady = 14)
playWithOther = Button(mainWindow, text = "PLAY WITH OTHER PLAYER", padx = 25, pady = 14, command = playWithOtherPlayer.openNewWindows)

playWithComp.grid(row=1,column=0, padx=8, pady=10)
playWithOther.grid(row=1,column=1)


mainWindow.mainloop()
