import tkinter as tk

def show_dashboard(username):
    root = tk.Tk()
    root.title("Engineer Social Dashboard")
    root.geometry("600x400")

    tk.Label(root, text="Welcome to Engineer Social!", font=("Helvetica", 18)).pack(pady=20)

    def open_activities():
        from activities import open_activities
        open_activities()

    def open_event_calendar():
        from event_calendar import open_calendar
        open_calendar(username)

    def open_bulletin():
        from bulletin import open_bulletin
        open_bulletin()

    def open_emergency():
        from emergency import open_emergency
        open_emergency()

    tk.Button(root, text="Activities", width=20, command=open_activities).pack(pady=5)
    tk.Button(root, text="Event Calendar", width=20, command=open_event_calendar).pack(pady=5)
    tk.Button(root, text="Bulletin Board", width=20, command=open_bulletin).pack(pady=5)
    tk.Button(root, text="Emergency Contacts", width=20, command=open_emergency).pack(pady=5)

    root.mainloop()
