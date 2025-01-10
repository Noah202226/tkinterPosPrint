import tkinter as tk

def show_main_window():
    """Show the main application window."""
    main_window = tk.Tk()
    main_window.title("Main Window")
    label = tk.Label(main_window, text="Welcome to the Main Application!")
    label.pack(pady=20)
    main_window.mainloop()
