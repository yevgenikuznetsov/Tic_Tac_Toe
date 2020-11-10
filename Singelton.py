from tkinter import messagebox


class Singleton:
   __instance__ = None
   openNewWindow = False

   def __init__(self):
       if Singleton.__instance__ is None:
           Singleton.__instance__ = self

       else:
           Singleton.openNewWindow = True
           messagebox.showerror("Tic Tac Toe", "You can't open more than one window")

   @staticmethod
   def get_instance():
       if not Singleton.__instance__:
           Singleton()
       return Singleton.__instance__