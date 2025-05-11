from login.control import LoginController
from signup.control import SignupController
from tkinter import *
import customtkinter as ctk
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("800x400")
app = LoginController(root)
root.mainloop()


	
