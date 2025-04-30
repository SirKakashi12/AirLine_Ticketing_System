from login.control import LoginController
from signup.control import SignupController
from tkinter import *
import  customtkinter as tk



root = Tk()

root.geometry("800x400")
root.configure(bg="#ecbbdf")


app = LoginController(root)
root.mainloop()
