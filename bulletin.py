import tkinter as tk
from tkinter import messagebox

posts = []

def open_bulletin():
    win = tk.Toplevel()
    win.title("Bulletin Board")
    win.geometry("500x450")

    entry = tk.Entry(win, width=50)
    entry.pack(pady=10)

    board = tk.Listbox(win, width=60)
    board.pack()

    def post():
        text = entry.get()
        if text:
            posts.append(text)
            refresh()
            entry.delete(0, tk.END)

    def delete():
        try:
            index = board.curselection()[0]
            del posts[index]
            refresh()
            entry.delete(0, tk.END)
        except IndexError:
            messagebox.showerror("Error", "Select a post to delete.")

    def edit():
        try:
            index = board.curselection()[0]
            entry.delete(0, tk.END)
            entry.insert(0, posts[index])
        except IndexError:
            messagebox.showerror("Error", "Select a post to edit.")

    def update():
        try:
            index = board.curselection()[0]
            new_text = entry.get()
            if new_text:
                posts[index] = new_text
                refresh()
                entry.delete(0, tk.END)
        except IndexError:
            messagebox.showerror("Error", "Select a post to update.")

    def refresh():
        board.delete(0, tk.END)
        for item in posts:
            board.insert(tk.END, item)

    tk.Button(win, text="Post", command=post).pack(pady=2)
    tk.Button(win, text="Edit Selected", command=edit).pack(pady=2)
    tk.Button(win, text="Update Edited", command=update).pack(pady=2)
    tk.Button(win, text="Delete", command=delete).pack(pady=2)

    refresh()
