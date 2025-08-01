import tkinter as tk
from tkinter import messagebox
import sqlite3

DB_PATH = "db/app.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def open_activities():
    window = tk.Toplevel()
    window.title("Weekly Activities")
    window.geometry("500x500")

    entry = tk.Entry(window, width=50)
    entry.pack(pady=10)

    listbox = tk.Listbox(window, width=60)
    listbox.pack()

    def load_data():
        listbox.delete(0, tk.END)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, content FROM activities")
        for row in cursor.fetchall():
            listbox.insert(tk.END, f"{row[0]} - {row[1]}")
        conn.close()

    def add():
        text = entry.get()
        if text:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO activities (content) VALUES (?)", (text,))
            conn.commit()
            conn.close()
            load_data()
            entry.delete(0, tk.END)

    def delete():
        try:
            selected = listbox.get(listbox.curselection())
            activity_id = selected.split(" - ")[0]
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM activities WHERE id=?", (activity_id,))
            conn.commit()
            conn.close()
            load_data()
            entry.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "No item selected.")

    def edit():
        try:
            selected = listbox.get(listbox.curselection())
            content = selected.split(" - ", 1)[1]
            entry.delete(0, tk.END)
            entry.insert(0, content)
        except:
            messagebox.showerror("Error", "No item selected.")

    def update():
        try:
            selected = listbox.get(listbox.curselection())
            activity_id = selected.split(" - ")[0]
            new_text = entry.get()
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE activities SET content=? WHERE id=?", (new_text, activity_id))
            conn.commit()
            conn.close()
            load_data()
            entry.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Select an item first.")

    tk.Button(window, text="Add Activity", command=add).pack(pady=2)
    tk.Button(window, text="Edit Selected", command=edit).pack(pady=2)
    tk.Button(window, text="Update Edited", command=update).pack(pady=2)
    tk.Button(window, text="Delete Selected", command=delete).pack(pady=2)

    load_data()
