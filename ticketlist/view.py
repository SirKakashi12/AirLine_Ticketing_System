import customtkinter as ctk
from tkinter import Canvas, Scrollbar, ttk
from PIL import Image, ImageTk
import ticketlist.control as controller
import ticketlist.model as model
import session.session as session
import tkinter as tk


class TicketlistView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.geometry("1000x600")
        self.root.title("Ticket")
        self.id = session.Session.get('usrId')
        self.base_logo_image = Image.open("picture/logodm.png")

        ticket_data_list = controller.tickets_info(self.id)
        back_button = ctk.CTkButton(
            self.root,
            text="← Back",
            fg_color="#333333",
            hover_color="#555555",
            text_color="white",
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.go_back
        )
        back_button.pack(anchor="nw", padx=20, pady=(20, 0))
        # SCROLL FRAME
        self.scroll_frame = ctk.CTkScrollableFrame(self.root, width=900, bg_color="#000000")
        self.scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)

        if not ticket_data_list:
            no_ticket_label = ctk.CTkLabel(
                self.scroll_frame,
                text="Don't have Tickets yet",
                font=ctk.CTkFont(size=20, weight="bold"),
                text_color="#ff3333"
            )
            no_ticket_label.pack(pady=20)
        else:
            for data in ticket_data_list:
                username, airplane_name, airplane_code, dep_time, dep_date, arr_time, arr_date, dest, from_city, to_city, seat, flight_class,ticket_id = data
                card = ctk.CTkFrame(self.scroll_frame, corner_radius=15, fg_color="#1a1a1a", border_width=2, border_color="#ff3333")
                card.pack(fill="x", pady=10, padx=10)

                

                info_frame = ctk.CTkFrame(card, fg_color="transparent")
                info_frame.pack(fill="both", expand=True, padx=10, pady=10, side="left")

                ctk.CTkLabel(info_frame, text=f"Username: {username}", font=ctk.CTkFont(size=16, weight="bold"), text_color="white").pack(anchor="w")
                ctk.CTkLabel(info_frame, text=f"Plane: {airplane_name} ({airplane_code})", font=ctk.CTkFont(size=14), text_color="white").pack(anchor="w")
                ctk.CTkLabel(info_frame, text=f"Departure: {dep_date} at {dep_time} | Arrival: {arr_date} at {arr_time}", font=ctk.CTkFont(size=13), text_color="#cccccc").pack(anchor="w")
                ctk.CTkLabel(info_frame, text=f"From: {from_city} → To: {to_city} | Final Destination: {dest}", font=ctk.CTkFont(size=13), text_color="#cccccc").pack(anchor="w")
                ctk.CTkLabel(info_frame, text=f"Seat: {seat} | Class: {flight_class}", font=ctk.CTkFont(size=13), text_color="#ff3333").pack(anchor="w")

                logo_label = ctk.CTkLabel(card, text="")
                logo_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

                card.bind("<Configure>", lambda e, c=card, l=logo_label: self.resize_logo(e, c, l))

                cancel_button = ctk.CTkButton(
                    card,  
                    text="Cancel Ticket",
                    fg_color="#ff3333",
                    hover_color="#cc0000",
                    text_color="white",
                    font=ctk.CTkFont(size=12, weight="bold"),
                    command=lambda ticket_id=ticket_id : self.cancel_ticket(ticket_id)
                )
                cancel_button.place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)
               

    def resize_logo(self, event, card, logo_label):
        width = card.winfo_width()
        new_width = min(120, int(width * 0.2))
        new_height = int(new_width * self.base_logo_image.height / self.base_logo_image.width)

        resized_image = self.base_logo_image.resize((new_width, new_height), Image.LANCZOS)
        logo_ctk_image = ctk.CTkImage(light_image=resized_image, size=(new_width, new_height))
        logo_label.configure(image=logo_ctk_image)
        logo_label.image = logo_ctk_image


    def cancel_ticket(self,ticket_id ):
        self.controller.delete_ticket(ticket_id)   
         
    

    def go_back(self):
        self.controller.go_to_dashboard()
