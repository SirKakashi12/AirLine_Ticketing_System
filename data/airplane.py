import sqlite3
import random

def start():
    airplane_names = [
        "Boeing 737", "Airbus A320", "Boeing 777", "Airbus A350",
        "Cessna 172", "Bombardier CRJ", "Embraer E190", "Boeing 787",
        "Airbus A330", "McDonnell Douglas MD-80"
    ]

    conn = sqlite3.connect("database/Project.db")
    cursor = conn.cursor()

    # Optional: clear table first if needed
    # cursor.execute("DELETE FROM airplanes")

    for name in airplane_names:
        code = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=5))
        cursor.execute("""
            INSERT INTO airplanes (airplane_name, airplane_code)
            VALUES (?, ?)
        """, (name, code))

    conn.commit()
    conn.close()
