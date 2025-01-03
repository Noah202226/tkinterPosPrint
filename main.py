import tkinter as tk
from tkinter import messagebox
import win32print
import win32api

def get_printer_list():
    """Fetch the list of available printers."""
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
    return [printer[2] for printer in printers]

def print_text():
    """Print the entered text to the selected printer."""
    selected_printer = printer_var.get()
    text = text_area.get("1.0", tk.END).strip()
    
    if not selected_printer:
        messagebox.showerror("Error", "Please select a printer.")
        return
    if not text:
        messagebox.showerror("Error", "Text area is empty.")
        return
    
    # Add extra newlines to ensure text is fully printed
    text += "\n\n\n"  # Adding blank lines as margin

    try:
        # Set the selected printer
        win32print.SetDefaultPrinter(selected_printer)
        
        # Print the text
        handle = win32print.OpenPrinter(selected_printer)
        job = win32print.StartDocPrinter(handle, 1, ("Thermal Print Job", None, "RAW"))
        win32print.StartPagePrinter(handle)
        win32print.WritePrinter(handle, text.encode('utf-8'))
        win32print.EndPagePrinter(handle)
        win32print.EndDocPrinter(handle)
        win32print.ClosePrinter(handle)
        
        messagebox.showinfo("Success", "Text sent to printer successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to print. {e}")

# Create the main window
root = tk.Tk()
root.title("Thermal Printer GUI")

# Printer selection
printer_label = tk.Label(root, text="Select Printer:")
printer_label.pack(pady=5)

printer_var = tk.StringVar()
printer_dropdown = tk.OptionMenu(root, printer_var, *get_printer_list())
printer_dropdown.pack(pady=5)

# Text area for input
text_label = tk.Label(root, text="Enter Text to Print:")
text_label.pack(pady=5)

text_area = tk.Text(root, height=10, width=40)
text_area.pack(pady=5)

# Print button
print_button = tk.Button(root, text="Print", command=print_text)
print_button.pack(pady=10)

# Run the GUI
root.mainloop()
