import sqlite3
import session.session as session


class LoginModel:
    def __init__(self):
        self.conn = sqlite3.connect("database/Project.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                userId INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                password TEXT NOT NULL,
                birthdate DATE NOT NULL,
                zipcode INTEGER
            )
        """)
        self.conn.commit()

    def Check_user_is_regesterd(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
         (username, password))
        return self.cursor.fetchone() is not None

    def set_userid_session(self, username, password):
        self.cursor.execute("SELECT userId FROM users WHERE username=? AND password=?", (username, password))
        result = self.cursor.fetchone() 
        if result:
            session.Session.set("usrId", result[0])  
            return True
        return False
        


