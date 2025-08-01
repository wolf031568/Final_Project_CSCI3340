import tkinter as tk

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
        root.destroy()
        import login  
        login.show_login()

    tk.Button(root, text="Register", command=register).pack(pady=10)

    root.mainloop()
