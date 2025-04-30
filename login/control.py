import login.view as view
import login.model as model
import signup.control as signup_control

from tkinter import messagebox

class LoginController:
    def __init__(self, root):
        self.root = root
        self.model = model.LoginModel()
        self.view = view.LoginView(root, self)

    def login_handdiling(self):
        username = self.view.usernameEntry.get()
        password = self.view.passwordEntry.get()
        
        if self.model.Check_user_is_regesterd(username, password):
            messagebox.showinfo("Login Successful", "Welcome! " + username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def go_to_signup(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        signup_control.SignupController(self.root)