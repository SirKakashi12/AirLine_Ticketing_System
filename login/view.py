from tkinter import *
import customtkinter
import login.control as controller

class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.geometry("800x400")
        self.root.title("Sign In")


# Lable
        self.loginLabel = customtkinter.CTkLabel(
                master = self.root,
                text="Sign In",
                font=("Courier New", 50),
                text_color="#ff0000",
                height=60,
                width=156,
                corner_radius=0,
        )
        self.loginLabel.place(x=280, y=20)

        self.usernameLable = customtkinter.CTkLabel(
                master = self.root,
                text="username",
                font=("Courier New", 17),
                text_color="#ff0000",
                height=13,
                width=89,
                corner_radius=0,
                )
        self.usernameLable.place(x=270, y=100)

        self.passwordLabel = customtkinter.CTkLabel(
                master = self.root,
                text="passwrod",
                font=("Courier New", 17),
                text_color="#ff0000",
                height=18,
                width=89,
                corner_radius=0,
        )
        self.passwordLabel.place(x=270, y=160)   
#button
        self.exitBtn = customtkinter.CTkButton(
                master = self.root,
                text="Exit",
                font=("Courier New", 14),
                text_color="white",
                hover=True,
                hover_color="#ff0000",
                height=26,
                width=64,
                border_width=2,
                corner_radius=6,
                border_color="black",
                bg_color="transparent",
                fg_color="red",
                command = self.root.quit
        )
        self.exitBtn.place(x=730, y=10)

        self.loginBtn = customtkinter.CTkButton(
                master = self.root,
                text="Log In",
                font=("Courier New", 14),
                text_color="white",
                hover=True,
                hover_color="#ff0000",  # red on hover
                height=26,
                width=64,
                border_width=2,
                corner_radius=6,
                border_color="black",
                bg_color="transparent",
                fg_color="red",
                command =self.controller.login_handdiling ,
        )
        self.loginBtn.place(x=340, y=240)

        self.signupBtn = customtkinter.CTkButton(
                master = self.root,
                text="Sign Up",
                font=("Courier New", 14),
                text_color="white",
                hover=True,
                hover_color="#ff0000",
                height=26,
                width=64,
                border_width=2,
                corner_radius=6,
                border_color="black",
                bg_color="transparent",
                fg_color="red",
                command = self.controller.go_to_signup,
        )
        self.signupBtn.place(x=725, y=40)

#entry


        self.usernameEntry = customtkinter.CTkEntry(
                master = self.root,
                placeholder_text="username",
                placeholder_text_color="white",
                font=("Arial", 14),
                text_color="#000000",
                height=30,
                width=195,
                border_width=2,
                corner_radius=6,
                border_color="#000000",
        )
        self.usernameEntry.place(x=290, y=120)

        self.passwordEntry = customtkinter.CTkEntry(
                master = self.root,
                placeholder_text="password",
                placeholder_text_color="white",
                font=("Arial", 14),
                text_color="#000000",
                height=30,
                width=195,
                border_width=2,
                corner_radius=6,
                border_color="#000000",
        )
        self.passwordEntry.place(x=290, y=180)

   