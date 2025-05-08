import sqlite3

class SignModel:
    def __init__(self):
        self.conn = sqlite3.connect("database/Project.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                userId INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                password TEXT NOT NULL,
                birthdate TEXT NOT NULL,
                zipcode INTEGER
            )
        """)
        self.conn.commit()

    def check_if_username_is_taken(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone() is not None

    def signup_user(self, username, password, birthdate):
        self.cursor.execute(
            "INSERT INTO users (username, password, birthdate) VALUES (?, ?, ?)",
            (username, password, birthdate)
        )
        self.conn.commit()
