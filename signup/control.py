import signup.view as view
import signup.model as model
import login.control as login_control
from tkinter import messagebox

class SignupController:
    def __init__(self, root):
        self.root = root
        self.model = model.SignModel()
        self.view = view.SignupView(root, self)


    def regester_user_handeling(self):
        username = self.view.usernameEntry.get()
        password = self.view.passwordEntry.get()
        confirm_password = self.view.repeatPasswordEntry.get()
        birthdate = self.view.birthdateEntry.get()

        if not username or not password or not confirm_password or not birthdate:
            messagebox.showerror("Error", "All fields are required.")
            return 
        

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return
        if self.model.check_if_username_is_taken(username):
            messagebox.showerror("Signup Failed", "Username already exists.")
        else:
            self.model.signup_user(username, password, birthdate)
            messagebox.showinfo("Signup Successful", "Your account has been created!")

    def go_to_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        login_control.LoginController(self.root)