import tkinter as tk
import win32print
import win32ui

import login_window

def send_test_print():
    """Send a test print to the thermal printer."""
    try:
        printer_name = win32print.GetDefaultPrinter()
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)
        hdc.StartDoc("Test Print")
        hdc.StartPage()
        hdc.TextOut(100, 100, "Test Print: Thermal Printer Working")
        hdc.EndPage()
        hdc.EndDoc()
        hdc.DeleteDC()
        print("Test print sent successfully!")
    except Exception as e:
        print(f"Error sending test print: {e}")

def logout(pos_window):
    """Log out and close the POS window."""
    pos_window.quit()
    pos_window.destroy()

    login_window.show_login_window()

def show_main_window():
    """Show the main POS system window."""
    pos_window = tk.Tk()
    pos_window.title("POS System")

    pos_window.attributes("-fullscreen", True)
    pos_window.configure(bg="#f0f0f0")

    # Header Frame for Title
    header_frame = tk.Frame(pos_window, bg="#4CAF50", height=80, relief="raised")
    header_frame.pack(fill="x")

    title_label = tk.Label(header_frame, text="Point of Sale System", font=("Helvetica", 24, "bold"), fg="white", bg="#4CAF50")
    title_label.pack(pady=20)

    main_frame = tk.Frame(pos_window)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    left_frame = tk.Frame(main_frame, width=400, bg="#ffffff", relief="solid")
    left_frame.pack(side="left", fill="y", padx=10, pady=10)

    right_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid")
    right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # Left Frame: Orders and Details
    orders_label = tk.Label(left_frame, text="Order Details", font=("Helvetica", 16), bg="#ffffff")
    orders_label.pack(pady=10)

    order_listbox = tk.Listbox(left_frame, height=20, width=50, font=("Helvetica", 12))
    order_listbox.pack(padx=10, pady=10)

    example_orders = ["Order 1 - $50", "Order 2 - $100", "Order 3 - $150"]
    for order in example_orders:
        order_listbox.insert(tk.END, order)

    total_label = tk.Label(left_frame, text="Total: $300", font=("Helvetica", 14), bg="#ffffff")
    total_label.pack(pady=10)

    discount_label = tk.Label(left_frame, text="Discount: $10", font=("Helvetica", 14), bg="#ffffff")
    discount_label.pack(pady=10)

    # Right Frame: Settings and Controls
    settings_label = tk.Label(right_frame, text="Settings & Controls", font=("Helvetica", 16), bg="#ffffff")
    settings_label.pack(pady=10)

    description_label = tk.Label(right_frame, text="Manage settings, apply discounts, and more.", wraplength=300, font=("Helvetica", 12), bg="#ffffff")
    description_label.pack(padx=10, pady=10)

    total_button = tk.Button(right_frame, text="Calculate Total", width=20, height=2, command=lambda: print("Total Calculated"))
    total_button.pack(pady=10)

    discount_button = tk.Button(right_frame, text="Apply Discount", width=20, height=2, command=lambda: print("Discount Applied"))
    discount_button.pack(pady=10)

    test_printer_button = tk.Button(right_frame, text="Test Printer", font=("Helvetica", 14), bg="#FF9800", fg="white", width=20, height=2, command=send_test_print)
    test_printer_button.pack(pady=10)

    # Admin Settings Section
    admin_settings_label = tk.Label(right_frame, text="Admin Settings", font=("Helvetica", 16, "underline"), bg="#ffffff")
    admin_settings_label.pack(pady=20)

    user_management_button = tk.Button(right_frame, text="User Management", width=20, height=2, command=lambda: print("User Management Opened"))
    user_management_button.pack(pady=10)

    pos_customization_button = tk.Button(right_frame, text="POS Customization", width=20, height=2, command=lambda: print("POS Customization Opened"))
    pos_customization_button.pack(pady=10)

    logout_button = tk.Button(right_frame, text="Logout", font=("Helvetica", 14), bg="#FF5722", fg="white", width=20, height=2, command=lambda: logout(pos_window))
    logout_button.pack(pady=10)

    pos_window.mainloop()


