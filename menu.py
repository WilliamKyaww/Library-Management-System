import tkinter as tk

def book_search():
    print("--Book Search chosen--")

def book_checkout():
    print("--Book Checkout chosen--")

def book_return():
    print("--Book Return chosen--")

def book_select():
    print("--Book Select chosen--")

def main_menu():
    root = tk.Tk()

    # Set window size
    root.geometry("800x600")

    # Create buttons
    search_button = tk.Button(root, text="Book Search", command=book_search, width=30, height=4)
    checkout_button = tk.Button(root, text="Book Checkout", command=book_checkout, width=30, height=4)
    return_button = tk.Button(root, text="Book Return", command=book_return, width=30, height=4)
    select_button = tk.Button(root, text="Book Select", command=book_select, width=30, height=4)

    # Set button font size
    button_font = ("Arial", 20)
    search_button.config(font=button_font)
    checkout_button.config(font=button_font)
    return_button.config(font=button_font)
    select_button.config(font=button_font)

    # Place buttons on the window
    search_button.pack(pady=20)
    checkout_button.pack(pady=20)
    return_button.pack(pady=20)
    select_button.pack(pady=20)

    root.mainloop()

# Run the main menu
main_menu()
