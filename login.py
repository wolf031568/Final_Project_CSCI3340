import tkinter as tk

def show_login():
    root = tk.Tk()
    root.title("Engineer Social App - Login")
    root.geometry("400x300")

    tk.Label(root, text="Login", font=("Helvetica", 16)).pack(pady=10)

    username = tk.Entry(root)
    username.pack(pady=5)
    username.insert(0, "Username")

    password = tk.Entry(root, show="*")
    password.pack(pady=5)
    password.insert(0, "Password")

    def login():
        if username.get() and password.get():
            root.destroy()
            from dashboard import show_dashboard  
            show_dashboard()

    def go_register():
        root.destroy()
        import register
        register.show_register()

    tk.Button(root, text="Login", command=login).pack(pady=10)
    tk.Button(root, text="Register", command=go_register).pack()

    root.mainloop()
