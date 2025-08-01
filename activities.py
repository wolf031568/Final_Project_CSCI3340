import tkinter as tk
from tkinter import messagebox

activities = []

def open_activities():
    window = tk.Toplevel()
    window.title("Weekly Activities")
    window.geometry("500x450")

    entry = tk.Entry(window, width=50)
    entry.pack(pady=10)

    listbox = tk.Listbox(window, width=60)
    listbox.pack()

    def add():
        act = entry.get()
        if act:
            activities.append(act)
            refresh()
            entry.delete(0, tk.END)

    def delete():
        try:
            index = listbox.curselection()[0]
            del activities[index]
            refresh()
            entry.delete(0, tk.END)
        except IndexError:
            messagebox.showerror("Error", "No activity selected.")

    def edit():
        try:
            index = listbox.curselection()[0]
            entry.delete(0, tk.END)
            entry.insert(0, activities[index])
        except IndexError:
            messagebox.showerror("Error", "Select an activity to edit.")

    def update():
        try:
            index = listbox.curselection()[0]
            new_text = entry.get()
            if new_text:
                activities[index] = new_text
                refresh()
                entry.delete(0, tk.END)
        except IndexError:
            messagebox.showerror("Error", "Select an activity to update.")

    def refresh():
        listbox.delete(0, tk.END)
        for act in activities:
            listbox.insert(tk.END, act)

    tk.Button(window, text="Add Activity", command=add).pack(pady=2)
    tk.Button(window, text="Edit Selected", command=edit).pack(pady=2)
    tk.Button(window, text="Update Edited", command=update).pack(pady=2)
    tk.Button(window, text="Delete Selected", command=delete).pack(pady=2)

    refresh()
