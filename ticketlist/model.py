import sqlite3
import session.session as session

class TicketlistModel:
	def __init__(self):
		self.conn = sqlite3.connect("database/Project.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute("PRAGMA foreign_keys = ON;")
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS users (
				userId INTEGER PRIMARY KEY AUTOINCREMENT,
				username VARCHAR(50) UNIQUE NOT NULL,
				password VARCHAR(50) NOT NULL
				)
			""")
		self.conn.commit()	 
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS airplanes (
				airplaneId INTEGER PRIMARY KEY AUTOINCREMENT,
				airplane_name VARCHAR(50),
				airplane_code VARCHAR(5)
				)
			""")
		self.conn.commit()	 
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
		self.conn.commit()	 
		self.cursor.execute("""
			CREATE TABLE IF NOT EXISTS tickets (
				ticketId INTEGER PRIMARY KEY AUTOINCREMENT,
				userId INTEGER,
				departuresId INTEGER,
				seat_code VARCHAR(5),
				class VARCHAR(15),
				FOREIGN KEY(userId) REFERENCES users(userId),
				FOREIGN KEY(departuresId) REFERENCES departures(departuresId)
				)
			""")
		self.conn.commit()	


	def fetch_all_tickets(self, id):
		self.cursor.execute("""
		SELECT 
		    u.username,
		    a.airplane_name,
		    a.airplane_code,
		    d.departure_time,
		    d.departure_date,
		    d.arrival_time,
		    d.arrival_date,
		    d.destination,
		    d.departure_city,
		    d.arrival_city,
		    t.seat_code,
		    t.class,
		    t.ticketId
		FROM tickets t
		JOIN users u ON t.userId = u.userId
		JOIN departures d ON t.departuresId = d.departuresId
		JOIN airplanes a ON d.airplaneId = a.airplaneId
		WHERE t.userId = ?
		""", (id,))
		return  self.cursor.fetchall()

	def ticketdel(self, ticket_id):
	    self.cursor.execute("""
	        DELETE FROM tickets
	        WHERE ticketId = ?
	    """, (ticket_id,))
	    self.conn.commit()

