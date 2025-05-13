import sqlite3
import session.session as session

class TicketModel:
	def __init__(self):
		self.conn = sqlite3.connect("database/Project.db")
		self.cursor = self.conn.cursor()
		self.cursor.execute("PRAGMA foreign_keys = ON;")
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
				FOREIGN KEY(departuresId) REFERENCES departures(departuresId),
				UNIQUE(seat_code)
				)
			""")
		self.conn.commit()
	def seat_is_taken(self, departuresId, seat_code):
	    self.cursor.execute("""
	        SELECT 1 FROM tickets 
	        WHERE departuresId = ? AND seat_code = ?
	    """, (departuresId, seat_code))
	    
	    return  self.cursor.fetchone() is not None


	def get_all_info_in_departure(self, departuresId):
		self.cursor.execute("""
			SELECT departuresId, departure_city, arrival_city, departure_time, departure_date, arrival_time, arrival_date, destination, airplaneId
			FROM departures
			WHERE departuresId = ?
			""", (departuresId,))
		
		row = self.cursor.fetchone() 
		if row:
			return {
			"departuresId": row[0],
			"from": row[1],
			"to": row[2],
			"departure_time": row[3],
			"departure_date": row[4],
			"boarding_time": row[5],
			"boarding_date": row[6],
			"destination": row[7],
			"airplaneId": row[8]
			}
		else:
			return None



	def Insert_Ticket_database(self, userId, departuresId, seat_code, classes):
		try:
		    self.cursor.execute("""
		        INSERT INTO tickets (userId, departuresId, seat_code, class)
		        VALUES (?, ?, ?, ?)
		    """, (userId, departuresId, seat_code, classes))
		    self.conn.commit()
		    return True
		except sqlite3.IntegrityError:
		    return False

	def remove_departureid_session(self):
		session.Session.remove("departuresId")
		return True   
