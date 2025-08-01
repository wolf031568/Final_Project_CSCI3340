import tkinter as tk
import sqlite3

#get list of clubs user is subscribed to
def get_user_subscriptions(username):
    conn = sqlite3.connect("db/app.db")
    cursor = conn.cursor()
    #Query for clubs the user is subscribed to
    cursor.execute("SELECT club FROM subscriptions WHERE username = ?", (username,))
    #assign the club name(s) from the table
    clubs = [row[0] for row in cursor.fetchall()]
    conn.close()
    return clubs
#update and check for the subscription status of the user
def update_subscription(username, club, is_checked):
    conn = sqlite3.connect("db/app.db")
    cursor = conn.cursor()
    #check subscription status and update the database
    if is_checked:
        cursor.execute("INSERT OR IGNORE INTO subscriptions (username, club) VALUES (?, ?)", (username, club))
    else:
        cursor.execute("DELETE FROM subscriptions WHERE username = ? AND club = ?", (username, club))

    conn.commit()
    conn.close()

def open_calendar(username):
    win = tk.Toplevel()
    win.title("Event Calendar")
    win.geometry("500x300")

    tk.Label(win, text="Engineering Event Calendar", font=("Arial", 16)).pack(pady=10)

    tk.Label(win, text=" Hackathon - Aug 10\n Robotics Club - Every Friday\n Civil Meet - Monthly 1st Monday").pack(pady=20)

    tk.Label(win, text="Subscribe to clubs:").pack()

    subscriptions = get_user_subscriptions(username)
    #dictionary for the club status 
    club_vars = {}
    def on_check(club):
        def inner():
            #when a checkbox is checked or unchecked, the subscription is updated
            update_subscription(username, club, club_vars[club].get())
        return inner
    for club in ["Robotics", "Civil", "Software", "Electrical"]:
        #toggle status check
        club_vars[club] = tk.BooleanVar(value=(club in subscriptions))
        cb = tk.Checkbutton(win, text=club, variable=club_vars[club], command=on_check(club))
        cb.pack() 
