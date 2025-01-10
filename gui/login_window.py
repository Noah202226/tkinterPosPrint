import tkinter as tk
from gui.main_window import show_main_window

def show_login_window():
    """Show the login window."""
    login_window = tk.Tk()
    login_window.title("Login")
    
    tk.Label(login_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(login_window).grid(row=0, column=1, padx=10, pady=10)
    
    tk.Label(login_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(login_window, show="*").grid(row=1, column=1, padx=10, pady=10)
    
    tk.Button(login_window, text="Login", command=lambda: login(login_window)).grid(row=2, columnspan=2, pady=10)
    login_window.mainloop()

def login(window):
    """Handle login and close the login window."""
    # Perform login verification here (e.g., check credentials)
    # For simplicity, we'll just close the window
    window.destroy()
    show_main_window()
