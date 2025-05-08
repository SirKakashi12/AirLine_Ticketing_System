import login.view as view
import login.model as model
import signup.control as signup_control
import dashboard.control as dashboard_control

from tkinter import messagebox

class LoginController:
    def __init__(self, root):
        self.root = root
        self.model = model.LoginModel()
        self.view = view.LoginView(root, self)

    def go_to_signup(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        signup_control.SignupController(self.root)


    def go_to_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        dashboard_control.DashboardController(self.root)


    def login_handdiling(self):
        username = self.view.usernameEntry.get()
        password = self.view.passwordEntry.get()
        
        if self.model.Check_user_is_regesterd(username, password):
            messagebox.showinfo("Login Successful", "Welcome! " + username)
            self.model.set_userid_session(username,password)
            self.go_to_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

