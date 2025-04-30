from tkinter import *
import customtkinter
import signup.control as controller
from tkcalendar import DateEntry

class SignupView:
	def __init__(self, root, controller):
		self.root = root
		self.controller = controller

		self.root.title("Sign up")

#Lable
		self.signupLable = customtkinter.CTkLabel(
			master=self.root,
			text="Sign up",
			font=("Courier New", 50),
			text_color="#ff0000",
			height=60,
			width=215,
			corner_radius=0,
			bg_color="#ecbbdf",
			fg_color="#ecbbdf",
		)
		self.signupLable.place(x=280, y=20)

		self.birthdateLable = customtkinter.CTkLabel(
			master=self.root,
			text="Birth Date",
			font=("Courier New", 14),
			text_color="#ff0000",
			height=18,
			width=90,
			corner_radius=0,
			bg_color="#ecbbdf",
			fg_color="#ecbbdf",
		)
		self.birthdateLable.place(x=270, y=250)

		self.confirmpasswordLable = customtkinter.CTkLabel(
			master=self.root,
			text="Confirm Password",
			font=("Courier New", 14),
			text_color="#ff0000",
			height=18,
			width=121,
			corner_radius=0,
			bg_color="#ecbbdf",
			fg_color="#ecbbdf",
		)
		self.confirmpasswordLable.place(x=270, y=200)

		self.usernameLable = customtkinter.CTkLabel(
			master=self.root,
			text="Username",
			font=("Courier New", 14),
			text_color="#ff0000",
			height=18,
			width=70,
			corner_radius=0,
			bg_color="#ecbbdf",
			fg_color="#ecbbdf",
		)
		self.usernameLable.place(x=270, y=100)

		self.passwrodLable = customtkinter.CTkLabel(
			master=self.root,
			text="Password",
			font=("Courier New", 14),
			text_color="#ff0000",
			height=18,
			width=68,
			corner_radius=0,
			bg_color="#ecbbdf",
			fg_color="#ecbbdf",
		)
		self.passwrodLable.place(x=270, y=150)

#Entry		

		self.passwordEntry = customtkinter.CTkEntry(
			master=self.root,
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
		self.passwordEntry.place(x=280, y=170)

		self.usernameEntry = customtkinter.CTkEntry(
			master=self.root,
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
		self.usernameEntry.place(x=280, y=120)

		self.repeatpasswordEntry = customtkinter.CTkEntry(
			master=self.root,
			placeholder_text="repeat password",
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
		self.repeatpasswordEntry.place(x=280, y=220)

		self.birthdateEntry = DateEntry(
		    master=self.root,
		    width=18,
		    background='darkblue',
		    foreground='white',
		    borderwidth=2,
		    date_pattern='yyyy-mm-dd'  # Format: YYYY-MM-DD
		)
		self.birthdateEntry.place(x=280, y=270)

#button
		self.signupBtn = customtkinter.CTkButton(
			master=self.root,
			text="Sign up",
			font=("undefined", 14),
			text_color="#ff00ff",
			hover=True,
			hover_color="#0000ff",
			height=30,
			width=95,
			border_width=2,
			corner_radius=6,
			border_color="#ff00ff",
			bg_color="#ecbbdf",
			fg_color="#F0F0F0",
			command = self.controller.regester_user_handeling
		)
		self.signupBtn.place(x=330, y=320)

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
			command = self.controller.go_to_login
		)
		self.loginBtn.place(x=730, y=40)


