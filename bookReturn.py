from database import read_log_file

def read_log_file():
    log_info = []
    log_file = open("logfile.txt", "r")

    for line in log_file:
        s = line.strip()
        strings = s.split(",")
        log_info.append(strings)

    log_file.close()
    return log_info


def validate_book_id():
    valid_book_id = False

    while not valid_book_id:
        book_id = str(input("Enter book ID to return: "))

        if not book_id.isdigit() or int(book_id) < 1 or int(book_id) > 20:
            print("\33[91m--Error: Invalid book ID--\33[0m")
        else:
            print("\33[92m--Valid book ID--\33[0m")
            valid_book_id = True

    return book_id


def find_book_ids(log_info, book_id):
    book_id_list = []
    exist = False

    for log in log_info:
        if book_id == log[0]:
            exist = True
            book_id_list.append(log)

    return book_id_list, exist


def book_return():
    print("\33[92m--Book Return chosen\33[0m--")

    log_info = read_log_file()
    book_id = validate_book_id()

    book_id_list, exist = find_book_ids(log_info, book_id)

    if exist:
        if book_id_list[-1][4] == "Unavailable":
            print()
            print("Book ID", book_id, "has been returned.")

            if book_id_list[-1][5] == "Reserved":
                print("The returned book is reserved by a member.")
        else:
            print()
            print("--\33[91mBook ID", book_id, "currently available.\33[0m--")
            print("--\33[91mBook ID:", book_id, "cannot be returned.\33[0m--")
    else:
        print("\33[91m--Error: Book ID not found--\33[0m")

    # Update database changes
    log_file = open("logfile.txt", "a")
    from datetime import date
    return_date = str(date.today().day) + "-" + str(date.today().month) + "-" + str(date.today().year)
    newline = (
            "\n"
            + book_id_list[-1][0]
            + ","
            + book_id_list[-1][1]
            + ","
            + book_id_list[-1][2]
            + ","
            + return_date
            + ",Available,"
            + book_id_list[-1][5]
    )
    if book_id_list[-1][4] == "Unavailable":
        log_file.write(newline)

    log_file.close()


# Call the function
book_return()
