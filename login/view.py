from tkinter import *
import customtkinter
import login.control as controller

class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.root.title("Tkinter")
        self.root.geometry("800x400")
        self.root.configure(bg="#ecbbdf")

# Lable
        self.loginLabel = customtkinter.CTkLabel(
        master = self.root,
        text="Login",
        font=("Courier New", 50),
        text_color="#ff0000",
        height=60,
        width=156,
        corner_radius=0,
        bg_color="#ecbbdf",
        fg_color="#ecbbdf",
        )
        self.loginLabel.place(x=310, y=20)

        self.usernameLable = customtkinter.CTkLabel(
        master = self.root,
        text="username",
        font=("Courier New", 17),
        text_color="#ff0000",
        height=13,
        width=89,
        corner_radius=0,
        bg_color="#ecbbdf",
        fg_color="#ecbbdf",
        )
        self.usernameLable.place(x=270, y=100)

        self.passwordLabel = customtkinter.CTkLabel(
        master = self.root,
        text="passwrod",
        font=("Courier New", 14),
        text_color="#ff0000",
        height=18,
        width=89,
        corner_radius=0,
        bg_color="#ecbbdf",
        fg_color="#ecbbdf",
        )
        self.passwordLabel.place(x=270, y=160)   
#button
        self.exitBtn = customtkinter.CTkButton(
        master = self.root,
        text="Exit",
        font=("undefined", 14),
        text_color="#ff00ff",
        hover=True,
        hover_color="#0000ff",
        height=26,
        width=64,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#ecbbdf",
        fg_color="#F0F0F0",
        command = self.root.quit
        )
        self.exitBtn.place(x=730, y=10)

        self.loginBtn = customtkinter.CTkButton(
        master = self.root,
        text="Log In",
        font=("undefined", 14),
        text_color="#e100ff",
        hover=True,
        hover_color="#0000ff",
        height=30,
        width=95,
        border_width=2,
        corner_radius=6,
        border_color="#ff00ff",
        bg_color="#ecbbdf",
        fg_color="#F0F0F0",
        command =self.controller.login ,
        )
        self.loginBtn.place(x=340, y=240)

        self.signupBtn = customtkinter.CTkButton(
        master = self.root,
        text="Sign Up",
        font=("undefined", 14),
        text_color="#ff00ff",
        hover=True,
        hover_color="#0000ff",
        height=26,
        width=64,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#ecbbdf",
        fg_color="#F0F0F0",
        )
        self.signupBtn.place(x=730, y=40)

#entry


        self.usernameEntry = customtkinter.CTkEntry(
        master = self.root,
        placeholder_text="username",
        placeholder_text_color="#454545",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=195,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#ecbbdf",
        fg_color="#F0F0F0",
        )
        self.usernameEntry.place(x=290, y=120)

        self.passwordEntry = customtkinter.CTkEntry(
        master = self.root,
        placeholder_text="password",
        placeholder_text_color="#454545",
        font=("Arial", 14),
        text_color="#000000",
        height=30,
        width=195,
        border_width=2,
        corner_radius=6,
        border_color="#000000",
        bg_color="#ecbbdf",
        fg_color="#F0F0F0",
        )
        self.passwordEntry.place(x=290, y=180)

   