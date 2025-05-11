import sqlite3
import session.session as session
import data.departure as departure
import data.airplane as airplane
class DashboardModel:
    def __init__(self):
        self.conn = sqlite3.connect("database/Project.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")
        self._initialize_tables()
        airplane.start()
        departure.start()

    def _initialize_tables(self):
        with self.conn:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                userId INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(50) NOT NULL
                )
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS airplanes (
                airplaneId INTEGER PRIMARY KEY AUTOINCREMENT,
                airplane_name VARCHAR(50),
                airplane_code VARCHAR(5)
                )
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS departures (
                departuresId INTEGER PRIMARY KEY AUTOINCREMENT,
                arrival_time TIME NOT NULL,  
                arrival_date DATE NOT NULL,
                departure_time TIME NOT NULL,
                departure_date DATE NOT NULL,
                airplaneId INTEGER,
                destination VARCHAR(50),
                departure_city VARCHAR(50),
                arrival_city VARCHAR(50),
                FOREIGN KEY(airplaneId) REFERENCES airplanes(airplaneId)
                )
            """)

            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                ticketId INTEGER PRIMARY KEY AUTOINCREMENT,
                userId INTEGER,
                departuresId INTEGER,
                seat_code VARCHAR(5),
                class VARCHAR(15),
                FOREIGN KEY(userId) REFERENCES users(userId),
                FOREIGN KEY(departuresId) REFERENCES departures(departuresId),
                UNIQUE(seat_code)
                )
            """)



    def get_username(self, id):
        self.cursor.execute("SELECT username FROM users WHERE userId=?", (id,))
        result = self.cursor.fetchone()
        if result:
            session.Session.set("username", result[0])
            return True
            return False


    def fetch_departures(self,departure_city,arrival_city):
        self.cursor.execute("""
            SELECT departuresId, departure_city, arrival_city, departure_time, departure_date
            FROM departures
            WHERE departure_city = ? AND arrival_city = ?
            """, (departure_city, arrival_city))

        return [
        {
        "departuresId" : row[0],
        "from": row[1],
        "to": row[2],
        "departure_time": row[3],
        "departure_date": row[4]
        }
        for row in self.cursor.fetchall()
        ]



    def set_departureid_session(self,id):
        result = id
        session.Session.set("departuresId", result)
        return True



    def remove_userid_session(self):
        session.Session.remove("usrId")
        return True   
