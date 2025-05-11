from itertools import permutations
import sqlite3
import random
from datetime import datetime, timedelta

def start():
    provinces = sorted([
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

    conn = sqlite3.connect("database/Project.db")
    cursor = conn.cursor()

    # Fetch real airplaneIds
    cursor.execute("SELECT airplaneId FROM airplanes")
    airplane_ids = [row[0] for row in cursor.fetchall()]

    def random_time():
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return f"{hour:02d}:{minute:02d}"

    def random_date(start=datetime(2025, 5, 10), days=30):
        date = start + timedelta(days=random.randint(0, days))
        return date.strftime("%Y-%m-%d")

    pairs = [pair for pair in permutations(provinces, 2)]
    random.shuffle(pairs)
    pairs = pairs[:500]   

    for departure, arrival in pairs:
        arrival_time = random_time()
        departure_time = random_time()
        arrival_date = random_date()
        departure_date = random_date()
        airplaneId = random.choice(airplane_ids)

        cursor.execute("""
            INSERT INTO departures (
                arrival_time, arrival_date, 
                departure_time, departure_date, 
                airplaneId, destination, 
                departure_city, arrival_city
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            arrival_time, arrival_date,
            departure_time, departure_date,
            airplaneId, arrival,
            departure, arrival
        ))

    conn.commit()
    conn.close()
