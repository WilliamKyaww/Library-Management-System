

def read_log_file():
    log_info = []
    log_file = open("logfile.txt", "r")

    for line in log_file:
        s = line.strip()
        strings = s.split(",")
        log_info.append(strings)

    log_file.close()
    return log_info


def read_book_info():
    book_info = []
    book_file = open("Book_Info.txt", "r")

    for line in book_file:
        s = line.strip()
        strings = s.split(":")
        book_info.append(strings)

    book_file.close()
    return book_info


