import tkinter as tk
from tkinter import messagebox
from database import read_log_file
from datetime import date

def verify_member_id():
    member_id = member_id_entry.get()
    if member_id.isdigit() and len(member_id) == 4:
        messagebox.showinfo("Valid member ID", "Valid member ID")
    else:
        messagebox.showerror("Invalid member ID", "Invalid member ID")

def verify_book_id():
    book_id = book_id_entry.get()
    if book_id.isdigit() and 1 <= int(book_id) <= 20:
        messagebox.showinfo("Valid book ID", "Valid book ID")
    else:
        messagebox.showerror("Invalid book ID", "Invalid book ID")

def find_book_ids(log_info, book_id):
    book_id_list = []
    for line in log_info:
        if str(book_id) == line[0]:
            book_id_list.append(line)
    return book_id_list

def book_checkout():
    log_info = read_log_file()
    member_id = member_id_entry.get()
    book_id = book_id_entry.get()
    book_id_list = find_book_ids(log_info, book_id)

    if len(book_id_list) > 0:
        if book_id_list[-1][4] == "Unavailable" and book_id_list[-1][5] == "Unreserved":
            reserve = messagebox.askquestion("Book Unavailable",
                                             "Book ID " + book_id + " is currently unavailable. " +
                                            "Would you like to reserve the book?")
            if reserve == "yes":
                messagebox.showinfo("Book Reserved", "Book reserved.")
            else:
                messagebox.showinfo("Book Not Reserved", "Book not reserved.")
        elif book_id_list[-1][4] == "Available" and book_id_list[-1][5] == "Unreserved":
            messagebox.showinfo("Book Available",
                                "Book ID " + book_id + " is currently available." +
                                " Book ID " + book_id + " is checked-out.")
        elif book_id_list[-1][4] == "Available" and book_id_list[-1][5] == "Reserved":
            messagebox.showinfo("Book Available",
                                "Book ID " + book_id + " is currently available. " +
                                "However Book ID " + book_id + " is currently reserved. " +
                                "Book ID " + book_id + " is not checked-out.")
    else:
        messagebox.showerror("Invalid book ID", "Invalid book ID")

    # Database Changes
    log_file = open("logfile.txt", "a")

    if book_id_list[-1][4] == "Available" and book_id_list[-1][5] == "Unreserved":
        today_date = str(date.today().day) + "-" + str(date.today().month) + "-" + str(date.today().year)
        new_line = "\n" + book_id + "," + member_id + "," + today_date + ",," + "Unavailable" + "," + "Unreserved"
        log_file.write(new_line)

    if book_id_list[-1][4] == "Unavailable" and book_id_list[-1][5] == "Unreserved":
        if reserve == "yes":
            new_line = (
                    "\n"
                    + book_id_list[-1][0]
                    + ","
                    + book_id_list[-1][1]
                    + ","
                    + book_id_list[-1][2]
                    + ","
                    + book_id_list[-1][3]
                    + ","
                    + book_id_list[-1][4]
                    + ","
                    + "Reserved"
            )
            log_file.write(new_line)

    log_file.close()

# Create the main window
window = tk.Tk()
window.title("Book Checkout")

# Create and place the member ID label and entry
member_id_label = tk.Label(window, text="Member ID:")
member_id_label.pack()
member_id_entry = tk.Entry(window)
member_id_entry.pack()

# Create and place the book ID label and entry
book_id_label = tk.Label(window, text="Book ID:")
book_id_label.pack()
book_id_entry = tk.Entry(window)
book_id_entry.pack()

# Create and place the Verify Member ID button
verify_member_id_button = tk.Button(window, text="Verify Member ID", command=verify_member_id, width=30, height=4)
verify_member_id_button.pack()

# Create and place the Verify Book ID button
verify_book_id_button = tk.Button(window, text="Verify Book ID", command=verify_book_id, width=30, height=4)
verify_book_id_button.pack()

# Create and place the Book Checkout button
book_checkout_button = tk.Button(window, text="Book Checkout", command=book_checkout, width=30, height=4)
book_checkout_button.pack()

# Run the main event loop
window.mainloop()


