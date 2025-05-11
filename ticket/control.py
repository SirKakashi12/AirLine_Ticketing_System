import ticket.view as view
import ticket.model as model
import dashboard.control as dashboard_control
from tkinter import messagebox

class TicketController:
    def __init__(self,root):
        self.root = root
        self.model = model.TicketModel()
        self.view = view.TicketView(root,self)

    def go_to_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        dashboard_control.DashboardController(self.root)

    def cancel_ticket(self):
        self.model.remove_departureid_session()
        self.go_to_dashboard()
        

    def create_ticket(self, userId, departuresId, seat_code, classes):
        try:
            x = self.model.Insert_Ticket_database(userId, departuresId, seat_code, classes)
            if x == False:
                messagebox.showwarning("Warning", f"Seat {seat_code} is already taken for this flight.")
                return
            messagebox.showinfo("Info", "Successfully created ticket")
            self.model.remove_departureid_session()
            self.go_to_dashboard()
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

        
