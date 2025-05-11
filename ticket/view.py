import customtkinter as ctk
from tkinter import Canvas, Scrollbar, ttk
from PIL import Image, ImageTk, ImageDraw
import ticket.control as controller
import session.session as session
import ticket.model as model
import tkinter as tk

class TicketView:
    def __init__(self,root,controller):  
        self.root = root
        self.controller = controller
        self.root.geometry("570x250")
        self.root.title("Ticket")

        self.flightclasses = ["Economy", "Premium Economy", "Business", "First Class"]

        self.seatForFirstClass = sorted([
            "1A", "1B", "1C", "1D",
            "2A", "2B", "2C", "2D",
            "3A", "3B", "3C", "3D"
        ])

        self.seatForBusiness = sorted([
            "4A", "4B", "4C", "4D", "4E", "4F", "4G",
            "5A", "5B", "5C", "5D", "5E", "5F", "5G",
            "6A", "6B", "6C", "6D", "6E", "6F", "6G",
            "7A", "7B", "7C", "7D", "7E", "7F", "7G"
        ])

        self.seatForPremium = sorted([
            "8A", "8B", "8C", "8D", "8E", "8F", "8G",
            "9A", "9B", "9C", "9D", "9E", "9F", "9G",
            "10A", "10B", "10C", "10D", "10E", "10F", "10G",
            "11A", "11B", "11C", "11D", "11E", "11F", "11G"
        ])

        self.seatForEconomy = sorted([
            "12A", "12B", "12C", "12D", "12E", "12F", "12G", "12H", "12I", "12J",
            "13A", "13B", "13C", "13D", "13E", "13F", "13G", "13H", "13I", "13J",
            "14A", "14B", "14C", "14D", "14E", "14F", "14G", "14H", "14I", "14J",
            "15A", "15B", "15C", "15D", "15E", "15F", "15G", "15H", "15I", "15J",
            "16A", "16B", "16C", "16D", "16E", "16F", "16G", "16H", "16I", "16J"
        ])

        self.userid = session.Session.get('usrId')
        self.model = model.TicketModel()
        
        self.id = session.Session.get('departuresId')
        self.datas = self.model.get_all_info_in_departure(self.id) 


        # Load and resize logo
        self.logo_img = Image.open("picture/logo.png")
        self.logo_img = self.logo_img.resize((250, 30)) 
        self.logo = ImageTk.PhotoImage(self.logo_img)

        # Outer Frame
        self.outer_frame = tk.Frame(root, bd=2, relief="solid")
        self.outer_frame.grid(padx=10, pady=10)

        # Left section
        self.left_frame = tk.Frame(self.outer_frame, bd=1, relief="solid", padx=5, pady=5)
        self.left_frame.grid(row=0, column=0, sticky="nsew")

        # Configuring columns for center alignment
        for col in range(5):
            self.left_frame.grid_columnconfigure(col, weight=1)

        # Barcode label
        self.barcode = tk.Label(self.left_frame, text="barcode", width=10, height=8, borderwidth=1, relief="solid")
        self.barcode.grid(row=0, column=0, rowspan=8, padx=5, pady=5)

        # Text labels
        
        self.selected_class = tk.StringVar()
        self.selected_class.set("Economy")
        self.create_dropdown(self.left_frame, self.selected_class, self.flightclasses, row=0, column=1, columnspan=4)

        self.selected_class.trace("w", self.Tracing_classes)

        tk.Label(self.left_frame, text="Boarding Class", font=("Arial", 9)).grid(row=1, column=1, columnspan=4)
        tk.Label(self.left_frame, text="", font=("Arial", 9)).grid(row=2, column=1, columnspan=4)

        tk.Label(self.left_frame, text=f"{self.datas['from']} ---", anchor="e", font=("Arial", 9)).grid(row=3, column=1)
        tk.Label(self.left_frame, text="PR 2868 ---", font=("Arial", 9)).grid(row=3, column=2)

        
        self.bbc = tk.Label(self.left_frame, text="D", font=("Arial", 9))
        self.bbc.grid(row=3, column=3, columnspan=2)

        tk.Label(self.left_frame, text=f"{self.datas["to"]} ---", anchor="e", font=("Arial", 9)).grid(row=4, column=1)
        tk.Label(self.left_frame, text=f"{self.datas['departure_date']} ---", font=("Arial", 9)).grid(row=4, column=2)

        self.selected_seat = tk.StringVar()
        self.selected_seat.set("12A")
        self.create_dropdown(self.left_frame, self.selected_seat, self.seatForEconomy, row=5, column=1, columnspan=4)

        self.selected_seat.trace("w", self.Tracing_seat )

       
        self.group = tk.Label(self.left_frame, text=f"{self.datas['airplaneId']}D ---", anchor="e", font=("Arial", 9))
        self.group .grid(row=6, column=2)
        self.seatNo1 = tk.Label(self.left_frame, text="12A", font=("Arial", 9))
        self.seatNo1.grid(row=6, column=3, columnspan=2)
        # Right Frame
        self.right_frame = tk.Frame(self.outer_frame, bd=2, relief="flat")
        self.right_frame.grid(row=0, column=1, sticky="n")

        tk.Label(self.right_frame, text="Boarding pass", width=20).grid(row=0, column=0, rowspan=2, columnspan=2)
        self.Economy = tk.Label(self.right_frame, text="Economy")
        self.Economy.grid(row=0, column=2, columnspan=3)
        self.EconomyClass = tk.Label(self.right_frame, text="Economy Class")
        self.EconomyClass.grid(row=1, column=2, columnspan=3)

        tk.Label(self.right_frame, text="FROM:").grid(row=2, column=0)
        tk.Label(self.right_frame, text=f"{self.datas['from']}").grid(row=2, column=1)
        tk.Label(self.right_frame, text="FLIGHT: PR 2868").grid(row=2, column=2, columnspan=2)

        self.bbc2 = tk.Label(self.right_frame, text="BBC: D")
        self.bbc2.grid(row=2, column=4)

        tk.Label(self.right_frame, text="TO:").grid(row=3, column=0)
        tk.Label(self.right_frame, text=f"{self.datas['to']}").grid(row=3, column=1)
        tk.Label(self.right_frame, text="Date:").grid(row=3, column=2)
        tk.Label(self.right_frame, text=f"{self.datas['departure_date']}").grid(row=3, column=3)

        tk.Label(self.right_frame, text="").grid(row=4, column=0, rowspan=2, columnspan=2)
        tk.Label(self.right_frame, text="Gate").grid(row=4, column=2)
        tk.Label(self.right_frame, text="Group").grid(row=4, column=3)
        tk.Label(self.right_frame, text="Seat").grid(row=4, column=4)

        tk.Label(self.right_frame, text=f"{self.datas['airplaneId']}").grid(row=5, column=2)
        self.group1 = tk.Label(self.right_frame, text=f"{self.datas['airplaneId']}"+"A")
        self.group1.grid(row=5, column=3)

        self.seatNo = tk.Label(self.right_frame, text="SeatNo*")
        self.seatNo.grid(row=5, column=4)

        tk.Label(self.right_frame, text="barcode", relief="solid", width=20, height=2).grid(row=6, column=0, rowspan=2, columnspan=2)
        tk.Label(self.right_frame, text="boarding Time").grid(row=6, column=2)
        tk.Label(self.right_frame, text=f"{self.datas['departure_time']}").grid(row=7, column=2)
        tk.Label(self.right_frame, text="SEQ:").grid(row=7, column=3)
        tk.Label(self.right_frame, text="Seq*", anchor="w").grid(row=7, column=4, sticky="w")

        # position Logo at the bottom right
        tk.Label(self.right_frame, image=self.logo).grid(row=8, column=0, columnspan=5, sticky="e", pady=(10, 0))




        self.bottom_frame = ctk.CTkFrame(root, fg_color="transparent")
        self.bottom_frame.grid(row=5, column=0, sticky="w", padx=20, pady=10)

        # Button inside bottom frame
        create_ticket_button = ctk.CTkButton(self.bottom_frame,  text="Create Ticket", command=self.CreatingTicketOnclick)
        create_ticket_button.grid(row=0, column=0, padx=10, pady=5)

        Cancel_ticket_button = ctk.CTkButton(self.bottom_frame, text="Cancel Ticket", command=controller.cancel_ticket )
        Cancel_ticket_button.grid(row=0, column=2, padx=10, pady=5)

    def CreatingTicketOnclick(self):
        try:
            userId = self.userid
            departuresId = self.id
            seat_code = self.selected_seat.get()
            classes = self.selected_class.get()
            print(userId,departuresId,seat_code,classes)
            if not seat_code:
                messagebox.showwarning("error", "somethings wrong in seat_code")
                return
            if not classes:
                messagebox.showwarning("error", "somethings wrong in classes")
                return
            self.controller.create_ticket(userId,departuresId,seat_code,classes)

        except AttributeError as e:
            messagebox.showerror("Error", f"error: {e}")

    def create_dropdown(self, root, variable, values, row, column, columnspan=1):
        dropdown = ttk.Combobox(root, textvariable=variable, values=values, state="readonly", width=20)
        dropdown.grid(row=row, column=column, columnspan=columnspan, sticky="nsew", padx=5, pady=2)
        return dropdown

    def Tracing_seat(self, *args):
        selected_seat = self.selected_seat.get()
        self.seatNo.config(text=selected_seat)
        self.seatNo1.config(text=selected_seat)


    def Tracing_classes(self, *args):
        selected_class = self.selected_class.get()
        if selected_class == "First Class":
            self.selected_seat.set("1A")
            self.seatNo.config(text="1A")
            self.Economy.config(text="First")
            self.EconomyClass.config(text="First Class")
            self.bbc.config(text="A")
            self.bbc2.config(text="BBC: A")
            self.group.config(text=f"{self.datas['airplaneId']}"+"A ---")
            self.group1.config(text=f"{self.datas['airplaneId']}"+"A ---")
            seat_values = self.seatForFirstClass
        elif selected_class == "Business":
            self.selected_seat.set("4A")
            self.seatNo.config(text="4A")
            self.Economy.config(text="Business")
            self.EconomyClass.config(text="Business Class")
            self.bbc.config(text="B")
            self.bbc2.config(text="BBC: B")
            self.group.config(text=f"{self.datas['airplaneId']}"+"B ---")
            self.group1.config(text=f"{self.datas['airplaneId']}"+"B ---")
            seat_values = self.seatForBusiness
        elif selected_class == "Premium Economy":
            self.selected_seat.set("8A")
            self.seatNo.config(text="8A")
            self.Economy.config(text="Premium Economy")
            self.EconomyClass.config(text="Premium Economy Class")
            self.bbc.config(text="C")
            self.bbc2.config(text="BBC: C")
            self.group.config(text=f"{self.datas['airplaneId']}"+"C ---")
            self.group1.config(text=f"{self.datas['airplaneId']}"+"C ---")
            seat_values = self.seatForPremium
        else:  # Default to Economy
            self.selected_seat.set("12A")
            self.seatNo.config(text="12A")
            self.Economy.config(text="Economy")
            self.EconomyClass.config(text="Economy Class")
            self.bbc.config(text="D")
            self.bbc2.config(text="BBC: D")
            self.group.config(text=f"{self.datas['airplaneId']}"+"D ---")
            self.group1.config(text=f"{self.datas['airplaneId']}"+"D ---")
            seat_values = self.seatForEconomy
        self.create_dropdown(self.left_frame, self.selected_seat, seat_values, 5, 1, columnspan=4)