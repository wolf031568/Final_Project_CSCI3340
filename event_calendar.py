import tkinter as tk

def open_calendar():
    win = tk.Toplevel()
    win.title("Event Calendar")
    win.geometry("500x300")

    tk.Label(win, text="Engineering Event Calendar", font=("Arial", 16)).pack(pady=10)

    tk.Label(win, text=" Hackathon - Aug 10\n Robotics Club - Every Friday\n Civil Meet - Monthly 1st Monday").pack(pady=20)

    tk.Label(win, text="Subscribe to clubs:").pack()
    for club in ["Robotics", "Civil", "Software", "Electrical"]:
        tk.Checkbutton(win, text=club).pack()
