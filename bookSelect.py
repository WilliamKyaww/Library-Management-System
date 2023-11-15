from database import read_log_file
from database import read_book_info
import matplotlib.pyplot as plt

def calculate_book_id_frequency(book_info, log_info):
    book_id_frequency = []
    counter = 0
    for j in range(len(book_info)):
        for i in range(len(log_info)):
            if book_info[j][0] == log_info[i][0]:
                counter += 1
        book_id_frequency.append(counter)
        counter = 0
    return book_id_frequency

def plot_book_id_frequency(book_id_frequency):
    book_id_axis = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
    plt.bar(book_id_axis, book_id_frequency)
    plt.title("Book ID Access Frequency")
    plt.ylabel("Frequency")
    plt.xlabel("Book ID")
    plt.show()

def calculate_genre_frequency(book_info, log_info, book_id_frequency):
    genre_counters = {"Romance": 0, "Classics": 0, "Contemporary": 0, "Nonfiction": 0, "Fiction": 0, "Fantasy": 0, "Mystery": 0}
    for i in range(len(book_info)):
        genre = book_info[i][1]
        genre_counters[genre] += book_id_frequency[i]
    return genre_counters

def plot_genre_frequency(genre_counters):
    genres = ['Romance', 'Classics', 'Contemporary', 'Nonfiction', 'Fiction', 'Fantasy', 'Mystery']
    genre_frequency = [genre_counters[genre] for genre in genres]
    plt.bar(genres, genre_frequency)
    plt.title("Book Genre Access Frequency")
    plt.ylabel("Frequency")
    plt.xlabel("Book Genre")
    plt.show()

def determine_most_accessed_books(book_info, book_id_frequency):
    book_dict = {i + 1: frequency for i, frequency in enumerate(book_id_frequency)}
    descending_book_dict = sorted(book_dict.items(), key=lambda kv: kv[1], reverse=True)
    print("The most famous books are:")
    for i in range(5):
        book_id = descending_book_dict[i][0]
        book_title = book_info[book_id - 1][2]
        access_frequency = descending_book_dict[i][1]
        print(f"\t{i+1}. Book ID {book_id} \"{book_title}\" - Accessed {access_frequency} times")

def determine_most_accessed_genre(genre_counters):
    best_genre_frequency = max(genre_counters.values())
    best_genre_list = [genre for genre, frequency in genre_counters.items() if frequency == best_genre_frequency]
    print("The most famous genre(s) are:")
    for genre in best_genre_list:
        print(f"\t• {genre} - Accessed {best_genre_frequency} times")

def recommend_books(book_info, descending_book_dict):
    print("The price of:")
    for i in range(5):
        book_id = descending_book_dict[i][0]
        book_price = book_info[book_id - 1][4]
        print(f"\tBook ID {book_id} is £{book_price}")

def recommend_books_by_budget(book_info, descending_book_dict):
    prices_list = [int(book_info[book_id - 1][4]) for book_id, _ in descending_book_dict]
    budget = int(input("Input budget: "))
    if budget < min(prices_list):
        print("--Insufficient funds--")
    else:
        print("Recommended to buy another copy of:")
        total_price = 0
        for book_id, _ in descending_book_dict:
            book_price = int(book_info[book_id - 1][4])
            if budget >= total_price + book_price:
                total_price += book_price
                if budget >= total_price:
                    book_title = book_info[book_id - 1][2]
                    print(f"\t\"{book_title}\" - £{book_price}")
                else:
                    break

        remaining_money = budget - total_price
        print(f"The total price of the recommended list is £{total_price}. You will have £{remaining_money} remaining based on your budget.")





def book_select():
    print("\33[92m--Book Select chosen\33[0m--")

    log_info = read_log_file()
    book_info = read_book_info()
    book_id_frequency = calculate_book_id_frequency(book_info, log_info)

    plot_book_id_frequency(book_id_frequency)

    genre_counters = calculate_genre_frequency(book_info, log_info, book_id_frequency)

    plot_genre_frequency(genre_counters)
    print()

    determine_most_accessed_books(book_info, book_id_frequency)
    print()

    determine_most_accessed_genre(genre_counters)
    print()

    descending_book_dict = sorted(enumerate(book_id_frequency, start=1), key=lambda x: x[1], reverse=True)

    #recommend_books(book_info, descending_book_dict)
    #print()

    recommend_books_by_budget(book_info, descending_book_dict)

# Call the function
book_select()













