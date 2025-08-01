import tkinter as tk
from tkinter import messagebox
import sqlite3

DB_PATH = "db/app.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def open_bulletin():
    win = tk.Toplevel()
    win.title("Bulletin Board")
    win.geometry("500x450")

    entry = tk.Entry(win, width=50)
    entry.pack(pady=10)

    board = tk.Listbox(win, width=60)
    board.pack()

    def load_data():
        board.delete(0, tk.END)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, content FROM bulletin")
        for row in cursor.fetchall():
            board.insert(tk.END, f"{row[0]} - {row[1]}")
        conn.close()

    def post():
        text = entry.get()
        if text:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO bulletin (content) VALUES (?)", (text,))
            conn.commit()
            conn.close()
            load_data()
            entry.delete(0, tk.END)

    def delete():
        try:
            selected = board.get(board.curselection())
            post_id = selected.split(" - ")[0]
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM bulletin WHERE id=?", (post_id,))
            conn.commit()
            conn.close()
            load_data()
            entry.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Select a post to delete.")

    def edit():
        try:
            selected = board.get(board.curselection())
            content = selected.split(" - ", 1)[1]
            entry.delete(0, tk.END)
            entry.insert(0, content)
        except:
            messagebox.showerror("Error", "Select a post to edit.")

    def update():
        try:
            selected = board.get(board.curselection())
            post_id = selected.split(" - ")[0]
            new_text = entry.get()
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE bulletin SET content=? WHERE id=?", (new_text, post_id))
            conn.commit()
            conn.close()
            load_data()
            entry.delete(0, tk.END)
        except:
            messagebox.showerror("Error", "Select a post to update.")

    tk.Button(win, text="Post", command=post).pack(pady=2)
    tk.Button(win, text="Edit Selected", command=edit).pack(pady=2)
    tk.Button(win, text="Update Edited", command=update).pack(pady=2)
    tk.Button(win, text="Delete", command=delete).pack(pady=2)

    load_data()
