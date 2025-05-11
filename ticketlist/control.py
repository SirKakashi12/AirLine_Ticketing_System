import ticketlist.view as view
import ticketlist.model as model
import dashboard.control as dashboard_control
from tkinter import messagebox

class TicketlistController:
    def __init__(self, root):
        self.root = root
        self.model = model.TicketlistModel()
        self.view = view.TicketlistView(root, self,)

    def go_to_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        dashboard_control.DashboardController(self.root)
        

    def tickets_info(self,id):
        return self.model.fetch_all_tickets(id)


    def delete_ticket(self,ticket_id):
        self.model.ticketdel(ticket_id)
        for widget in self.root.winfo_children():
            widget.destroy()
        TicketlistController(self.root)

     