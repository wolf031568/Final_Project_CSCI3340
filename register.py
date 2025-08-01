import tkinter as tk
from tkinter import messagebox
import sqlite3

DB_PATH = "db/app.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def show_register():
    root = tk.Tk()
    root.title("Register")
    root.geometry("400x350")

    tk.Label(root, text="Register Account", font=("Helvetica", 16)).pack(pady=10)

    entries = {}
    for field in ["Username", "Password", "Email", "Full Name"]:
        entry = tk.Entry(root)
        entry.pack(pady=5)
        entry.insert(0, field)
        entries[field] = entry

    def register():
        username = entries["Username"].get()
        password = entries["Password"].get()
        email = entries["Email"].get()
        full_name = entries["Full Name"].get()

        if not username or not password:
            messagebox.showerror("Error", "Username and Password required")
            return

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, email, full_name) VALUES (?, ?, ?, ?)",
                        (username, password, email, full_name))
            conn.commit()
            messagebox.showinfo("Success", "Registration successful. Please log in.")
            root.destroy()
            import login
            login.show_login()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists.")
        finally:
            conn.close()

    tk.Button(root, text="Register", command=register).pack(pady=10)

    root.mainloop()
