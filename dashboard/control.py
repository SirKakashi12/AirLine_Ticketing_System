import dashboard.view as view
import dashboard.model as model
from tkinter import messagebox
import session.session as session
import ticket.control as ticket_controller
import ticketlist.control as ticketlist_controller
import login.control as login_controller

class DashboardController:
    def __init__(self,root):
        self.root = root
        self.model = model.DashboardModel()
        self.view = view.DashboardView(root, self)
       

        self.user_id = session.Session.get('usrId')
        self.model.get_username(self.user_id)
        username = session.Session.get("username")
        self.view.update_name(username)



    def search_departures(self, from_city, to_city):
        results = self.model.fetch_departures(from_city, to_city)
        self.view.display_departure_results(results)

    def go_to_ticket(self,id):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.model.set_departureid_session(id)
        ticket_controller.TicketController(self.root)

    def go_to_ticketlist(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        ticketlist_controller.TicketlistController(self.root)


    def go_to_login(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        login_controller.LoginController(self.root) 
        return True


    def logOut(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        session.Session.clear()
        self.go_to_login()
