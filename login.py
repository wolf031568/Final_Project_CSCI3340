import tkinter as tk
from tkinter import messagebox
import sqlite3

DB_PATH = "db/app.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def show_login():
    root = tk.Tk()
    root.title("Engineer Social App - Login")
    root.geometry("400x300")

    tk.Label(root, text="Login", font=("Helvetica", 16)).pack(pady=10)

    username_entry = tk.Entry(root)
    username_entry.pack(pady=5)
    username_entry.insert(0, "Username")

    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)
    password_entry.insert(0, "Password")

    def login():
        username = username_entry.get()
        password = password_entry.get()

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Success", f"Welcome {username}!")
            root.destroy()
            from dashboard import show_dashboard
            show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def go_register():
        root.destroy()
        import register
        register.show_register()

    tk.Button(root, text="Login", command=login).pack(pady=10)
    tk.Button(root, text="Register", command=go_register).pack()

    root.mainloop()
