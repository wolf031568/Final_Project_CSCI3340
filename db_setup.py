import sqlite3
import os

def init_db():
    if not os.path.exists("db"):
        os.makedirs("db")

    conn = sqlite3.connect("db/app.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            full_name TEXT
        )
    """)

    # Activities table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)

    # Bulletin table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bulletin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    # Event Calender table to store user club subscriptions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        club TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
