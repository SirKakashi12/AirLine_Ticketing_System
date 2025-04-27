import login.view as view
import login.model as model
from tkinter import messagebox

class LoginController:
    def __init__(self, root):
        self.model = model.LoginModel()
        self.view = view.LoginView(root, self)

    def login(self):
        username = self.view.usernameEntry.get()
        password = self.view.passwordEntry.get()
        
        if self.model.Check_user_is_regesterd(username, password):
            messagebox.showinfo("Login Successful", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def signup(self):
        messagebox.showinfo("Sign Up", "Go to signup page (function not implemented yet)")
