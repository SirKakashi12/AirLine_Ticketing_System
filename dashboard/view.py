import tkinter as tk
import customtkinter as ctk
from tkinter import Canvas, Scrollbar, ttk
from PIL import Image, ImageTk, ImageDraw
import dashboard.control as controller
import session.session as session


class DashboardView:
    def __init__(self, root, controller):
        self.root = root
        self.root.geometry("1000x500")
        self.root.title("Philippines Airlines")
        self.controller = controller
        self.root.configure(bg="#242424")



        self.provinces = sorted([
            "Abra", "Agusan del Norte", "Agusan del Sur", "Aklan", "Albay", "Antique", "Apayao", "Aurora",
            "Basilan", "Bataan", "Batanes", "Batangas", "Benguet", "Biliran", "Bohol", "Bukidnon",
            "Bulacan", "Cagayan", "Camarines Norte", "Camarines Sur", "Camiguin", "Capiz", "Catanduanes",
            "Cavite", "Cebu", "Cotabato", "Davao de Oro", "Davao del Norte", "Davao del Sur", "Davao Occidental",
            "Davao Oriental", "Dinagat Islands", "Eastern Samar", "Guimaras", "Ifugao", "Ilocos Norte", "Ilocos Sur",
            "Iloilo", "Isabela", "Kalinga", "La Union", "Laguna", "Lanao del Norte", "Lanao del Sur", "Leyte",
            "Maguindanao del Norte", "Maguindanao del Sur", "Marinduque", "Masbate", "Metro Manila", "Misamis Occidental",
            "Misamis Oriental", "Mountain Province", "Negros Occidental", "Negros Oriental", "Northern Samar",
            "Nueva Ecija", "Nueva Vizcaya", "Occidental Mindoro", "Oriental Mindoro", "Palawan", "Pampanga",
            "Pangasinan", "Quezon", "Quirino", "Rizal", "Romblon", "Samar", "Sarangani", "Siquijor", "Sorsogon",
            "South Cotabato", "Southern Leyte", "Sultan Kudarat", "Sulu", "Surigao del Norte", "Surigao del Sur",
            "Tarlac", "Tawi-Tawi", "Zambales", "Zamboanga del Norte", "Zamboanga del Sur", "Zamboanga Sibugay"
        ])

        self.from_var = tk.StringVar(value="Select From")
        self.to_var = tk.StringVar(value="Select To")

        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

        self.dboard_picture = ImageTk.PhotoImage(Image.open("picture/dboard_picture.png").resize((600, 150)))
        self.profile_picture = self.make_circle("picture/default_pfp.jpg", (100, 100))

        # Create ttk style for Combobox
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TCombobox", fieldbackground="#242424", background="#242424")

        # LEFT PANEL
        self.left_panel = tk.Frame(self.root, relief="solid", bd=1, bg="#242424")
        self.left_panel.grid(row=0, column=0, rowspan=8, sticky="nsew")

        tk.Label(self.left_panel,fg="red",font=("Courier New",20,"bold"), image=self.profile_picture, bg="#242424").pack(fill="x")
        self.home_button = tk.Button(self.left_panel,fg="red",font=("Courier New",20,"bold"), text="Home", bg="#242424")
        self.home_button.pack(fill="x")

        self.Ticket_list = tk.Button(self.left_panel,fg="red",font=("Courier New",20,"bold"), text="Ticket List", bg="#242424",command=controller.go_to_ticketlist)
        self.Ticket_list.pack(fill="x")

        tk.Label(self.left_panel,fg="red",font=("Courier New",20,"bold"), text="", bg="#242424").pack(fill="x")
        tk.Label(self.left_panel,fg="red",font=("Courier New",20,"bold"), text="", bg="#242424").pack(fill="x")

        self.logout_button = tk.Button(self.left_panel,fg="red",font=("Courier New",20,"bold"), text="Logout", bg="#242424", command=controller.logOut)
        self.logout_button.pack(fill="x", side="bottom")

        self.settings_button = tk.Button(self.left_panel,fg="red",font=("Courier New",20,"bold"), text="Settings", bg="#242424")
        self.settings_button.pack(fill="x", side="bottom")

        # MAIN CONTENT
        tk.Label(self.root,fg="red",font=("Courier New",20,"bold"), image=self.dboard_picture, bg="#242424").grid(row=0, column=1, columnspan=3, sticky="nsew")
        tk.Label(self.root,fg="red",font=("Courier New",20,"bold"), text="Philippines Airlines", bg="#242424").grid(row=1, column=1, columnspan=3, sticky="nsew")
        
        self.username = tk.Label(self.root,fg="red",font=("Courier New",20,"bold"), text="Welcome user's name", bg="#242424")
        self.username.grid(row=2, column=1, columnspan=3, sticky="w")

        x = session.Session.get("username")

        tk.Label(self.root,fg="red",font=("Courier New",20,"bold"), text="Departure Filter :", anchor="w", bg="#242424").grid(row=3, column=1, columnspan=3, sticky="nsew")

        self.from_dropdown = self.create_dropdown(self.root, self.from_var, 4, 1)
        tk.Label(self.root,fg="red",font=("Courier New",20,"bold"), text="----->", bg="#242424").grid(row=4, column=2, sticky="nsew")
        self.to_dropdown = self.create_dropdown(self.root, self.to_var, 4, 3)

        self.search_button = tk.Button(self.root,
                                        fg="red",
                                        font=("Courier New",20,"bold"),
                                        text="Search",
                                        bg="#242424",
                                        command=self.search)
        self.search_button.grid(row=5, column=1, columnspan=3, sticky="nsew")

        # SCROLLABLE CANVAS
        canvas_frame = tk.Frame(self.root, bg="#242424")
        canvas_frame.grid(row=6, column=1, rowspan=2, columnspan=3, sticky="nsew")

        self.canvas = Canvas(canvas_frame, bg="#242424")
        self.scrollbar = Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#242424")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")



    def make_circle(self, img_path, size):
        img = Image.open(img_path).resize(size).convert("RGBA")
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size[0], size[1]), fill=255)
        img.putalpha(mask)
        return ImageTk.PhotoImage(img)

    def create_dropdown(self, root, variable, row, column):
        dropdown = ttk.Combobox(root, textvariable=variable, values=self.provinces, state="readonly", width=20)
        dropdown.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
        return dropdown

    def update_name(self,x):
        self.username.config(text=f"Welcome {x}")    

    def search(self):
        from_city = self.from_var.get()
        to_city = self.to_var.get()
        self.controller.search_departures(from_city, to_city)

    def display_departure_results(self, results):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not results:
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            self.scrollable_frame.grid_rowconfigure(0, weight=1)
            self.scrollable_frame.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(
                self.scrollable_frame,
                text="No results found.",
                text_color="#FF5555",
                fg_color="white",
                font=("Courier New", 16, "bold"),
                corner_radius=10,
                height=40,
                anchor="center",
                padx=10
            ).grid(row=0, column=0, pady=20, padx=20, sticky="we")

        for r in results:
            row_text = f"{r['from']} → {r['to']} | {r['departure_date']} at {r['departure_time']}"

            row_frame = ctk.CTkFrame(master=self.scrollable_frame, fg_color="transparent")
            row_frame.pack(pady=6, padx=10, fill="x")

            label = ctk.CTkLabel(
                master=row_frame,
                text=row_text,
                text_color="#FF5555",
                fg_color="white",
                font=("Courier New", 16, "bold"),
                corner_radius=10,
                height=40,
                anchor="w"
            )
            label.pack(side="left", fill="x", expand=True, padx=(0, 10))

            action_btn = ctk.CTkButton(
                master=row_frame,
                text="Create Ticket",
                text_color="white",
                fg_color="#4CAF50",
                hover_color="#45A049",
                font=("Arial", 14, "bold"),
                width=120,
                height=36,
                corner_radius=10,
                command=lambda departure_id=r['departuresId']: self.controller.go_to_ticket(departure_id)
            )
            action_btn.pack(side="right")
