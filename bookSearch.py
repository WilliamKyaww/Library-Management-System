from database import read_log_file
from database import read_book_info

def read_book_info():
    book_info = []
    book_file = open("Book_Info.txt", "r")

    for line in book_file:
        s = line.strip()
        strings = s.split(":")
        book_info.append(strings)

    book_file.close()
    return book_info


def read_log_file():
    log_info = []
    log_file = open("logfile.txt", "r")

    for line in log_file:
        s = line.strip()
        strings = s.split(",")
        log_info.append(strings)

    log_file.close()
    return log_info


def verify_book_name(book_info):
    valid_name = False

    while not valid_name:
        book_name = input("Input book name: ").lower()

        matched_books = []
        for book in book_info:
            if book_name in book[2].lower():  # Perform case-insensitive partial matching
                matched_books.append(book)

        if len(matched_books) == 0:
            print("\33[91m--Error: No matching book found--\33[0m")
        elif len(matched_books) == 1:
            matched_book = matched_books[0]
            print()
            print(
                "The book title is \"" + matched_book[2] + "\". The author is " + matched_book[3] + ". The genre is " + matched_book[1] + "."
            )
            valid_name = True
        else:
            print("\33[93m--Multiple books found--\33[0m")
            print("Please select one of the following books:")
            for i, book in enumerate(matched_books):
                print(f"{i + 1}. {book[2]}")

            choice = input("Enter the number of the book: ")
            if choice.isdigit() and int(choice) in range(1, len(matched_books) + 1):
                matched_book = matched_books[int(choice) - 1]
                print()
                print(
                    "The book title is \"" + matched_book[2] + "\". The author is " + matched_book[3] + ". The genre is " + matched_book[1] + "."
                )
                valid_name = True
            else:
                print("\33[91m--Error: Invalid choice--\33[0m")

    return matched_book[2]  # Return the full book name



def find_book_ids(book_info, log_info, book_name):
    book_id_list = []
    exist = False

    for book in book_info:
        if book_name.upper() == book[2].upper():
            for log in log_info:
                if book[0] == log[0]:
                    exist = True
                    book_id_list.append(log)

    return book_id_list, exist


def book_search():
    print("\33[92m--Book Search chosen\33[0m--")

    book_info = read_book_info()
    log_info = read_log_file()

    book_name = verify_book_name(book_info)

    book_id_list, exist = find_book_ids(book_info, log_info, book_name)

    if exist:
        if book_id_list[-1][4] == "Available":
            print("The book is currently available to loan.")
        else:
            print("The book is currently unavailable to loan.")
    else:
        print("\33[91m--Error: Book ID not found--\33[0m")


# Call the function
book_search()




