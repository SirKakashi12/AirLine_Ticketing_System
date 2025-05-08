import dashboard.view as view
import dashboard.model as model
from tkinter import messagebox
import session.session as session

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
 