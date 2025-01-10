import tkinter as tk
import win32print
import win32ui

def send_test_print():
    """Send a test print to the thermal printer."""
    try:
        printer_name = win32print.GetDefaultPrinter()  # Get the default printer
        hprinter = win32print.OpenPrinter(printer_name)
        printer_info = win32print.GetPrinter(hprinter, 2)  # Get printer info

        # Create a device context
        hdc = win32ui.CreateDC()
        hdc.CreatePrinterDC(printer_name)
        hdc.StartDoc("Test Print")
        hdc.StartPage()

        # Send a test message to the printer
        hdc.TextOut(20, 20, "Test Print: Thermal Printer Working")  # You can customize the message
        hdc.EndPage()
        hdc.EndDoc()
        hdc.DeleteDC()

        print("Test print sent successfully!")

    except Exception as e:
        print(f"Error sending test print: {e}")

def logout(pos_window):
    """Log out and close the POS window."""
    pos_window.quit()  # Exit the Tkinter main loop
    pos_window.destroy()  # Destroy the window

def show_main_window():
    """Show the main POS system window."""
    pos_window = tk.Tk()
    pos_window.title("POS System")

    # Make the window full screen
    pos_window.attributes("-fullscreen", True)
    pos_window.configure(bg="#f0f0f0")  # Light gray background for better contrast

    # Create a frame for the entire layout (split into two sections)
    main_frame = tk.Frame(pos_window)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Create the left frame for the list of orders
    left_frame = tk.Frame(main_frame, width=300, bg="#ffffff", relief="solid")
    left_frame.pack(side="left", fill="y", padx=10, pady=10)

    # Create the right frame for the command buttons
    right_frame = tk.Frame(main_frame, bg="#ffffff", relief="solid")
    right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # Add a label for the orders list
    orders_label = tk.Label(left_frame, text="Orders", font=("Helvetica", 16), bg="#ffffff")
    orders_label.pack(pady=10)

    # Create a listbox to show orders (You can customize with order details)
    order_listbox = tk.Listbox(left_frame, height=15, width=30, font=("Helvetica", 12))
    order_listbox.pack(padx=10, pady=10)

    # Example orders for the listbox
    example_orders = ["Order 1 - $50", "Order 2 - $100", "Order 3 - $150"]
    for order in example_orders:
        order_listbox.insert(tk.END, order)

    # Add a label and button for total amount in the right frame
    total_label = tk.Label(right_frame, text="Total Amount:", font=("Helvetica", 16), bg="#ffffff")
    total_label.pack(pady=10)

    total_amount_label = tk.Label(right_frame, text="$0.00", font=("Helvetica", 14), bg="#ffffff")
    total_amount_label.pack(pady=10)

    def calculate_total():
        """Calculate the total amount based on orders."""
        total = 50 + 100 + 150  # Example total calculation, modify with actual logic
        total_amount_label.config(text=f"${total:.2f}")

    total_button = tk.Button(right_frame, text="Calculate Total", command=calculate_total, width=20, height=2)
    total_button.pack(pady=20)

    # Add a label and button for applying discount
    discount_label = tk.Label(right_frame, text="Discount:", font=("Helvetica", 16), bg="#ffffff")
    discount_label.pack(pady=10)

    discount_amount_label = tk.Label(right_frame, text="$0.00", font=("Helvetica", 14), bg="#ffffff")
    discount_amount_label.pack(pady=10)

    def apply_discount():
        """Apply a discount and update total."""
        discount = 10  # Example discount, modify with actual logic
        total = 50 + 100 + 150 - discount
        discount_amount_label.config(text=f"-${discount:.2f}")
        total_amount_label.config(text=f"${total:.2f}")

    discount_button = tk.Button(right_frame, text="Apply Discount", command=apply_discount, width=20, height=2)
    discount_button.pack(pady=20)

    # Add a "Test Printer" button to the right frame to send a test print
    test_printer_button = tk.Button(right_frame, text="Test Printer", font=("Helvetica", 14), bg="#FF9800", fg="white", width=20, height=2, command=send_test_print)
    test_printer_button.pack(pady=20)

    # Add a "Logout" button to log out and close the app
    logout_button = tk.Button(right_frame, text="Logout", font=("Helvetica", 14), bg="#FF5722", fg="white", width=20, height=2, command=lambda: logout(pos_window))
    logout_button.pack(pady=20)

    # Start the Tkinter main loop
    pos_window.mainloop()

# Run the main POS window
show_main_window()
