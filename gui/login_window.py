import tkinter as tk
from gui.main_window import show_main_window
from mymongo.crud import login_user
from mymongo.database import get_database

def show_login_window():
    """Show the login window."""
    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    error_label = None

    username_entry.focus()

    def on_login():
        nonlocal error_label
        db = get_database()
        username = username_entry.get()
        password = password_entry.get()

         # If there's already an error, remove it before showing a new one
        if error_label:
            error_label.grid_forget()

        if login_user(db, "users", username, password):
            login_window.destroy()
            show_main_window()
        else:
            error_label = tk.Label(login_window, text="Invalid credentials", fg="red")
            error_label.grid(row=3, columnspan=2, pady=10)
            
            # Remove the error message after 3 seconds
            login_window.after(3000, error_label.grid_forget)
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
            username_entry.focus()

    tk.Button(login_window, text="Login", command=on_login).grid(row=2, columnspan=2, pady=10)
    login_window.mainloop()
