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
			text="Sign Up",
			font=("Courier New", 50),
			text_color="#ff0000",
			height=60,
			width=215,
			corner_radius=0,
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

			)
		self.passwrodLable.place(x=270, y=150)

		#Entry		

		self.usernameEntry = customtkinter.CTkEntry(
			master=self.root,
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
			master=self.root,
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
		self.passwordEntry.place(x=290, y=170)

		self.repeatPasswordEntry = customtkinter.CTkEntry(
			master=self.root,
			placeholder_text="repeat password",
			placeholder_text_color="white",
			font=("Arial", 14),
			text_color="#000000",
			height=30,
			width=195,
			border_width=2,
			corner_radius=6,
			border_color="#000000",
			)
		self.repeatPasswordEntry.place(x=290, y=220)

		self.birthdateEntry = DateEntry(
			master=self.root,
			width=18,
			background='darkblue',
			foreground='white',
			borderwidth=2,
				    date_pattern='yyyy-mm-dd'  # Format: YYYY-MM-DD
				    )
		self.birthdateEntry.place(x=370, y=340)

		#button
		self.signupBtn = customtkinter.CTkButton(
			master=self.root,
			text="Sign Up",
			font=("Courier New", 14),
					text_color="#ffffff",  # white text for contrast
					hover=True,
					hover_color="#ff0000",  # red on hover
					height=30,
					width=95,
					border_width=2,
					corner_radius=6,
					border_color="black",
					bg_color="transparent",
					fg_color="red",
					command = self.controller.regester_user_handeling
					)
		self.signupBtn.place(x=330, y=320)

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
					command = self.controller.go_to_login
					)
		self.loginBtn.place(x=730, y=40)