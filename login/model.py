import sqlite3

class LoginModel:
    def __init__(self):
        self.conn = sqlite3.connect("database/users.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                usrId INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password TEXT NOT NULL,
                birthdate DATE NOT NULL
            )
        """)
        self.conn.commit()

    def Check_user_is_regesterd(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
         (username, password))
        return self.cursor.fetchone() is not None
