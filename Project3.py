#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author: Bodhi Fox
# CIST2110-001-Project-3 Library Management System (LMS)
# Project 3 will implement a library management system (LMS) that will allow users to manage books, users, and a library to manage collection of books and users.
# The LMS will be menu driven and will allow users to add, delete, and update books and users.
# Users will also be able to borrow and return books.
# The LMS will also allow users to search for books and users.

# ENABLE WORD WRAP TO MAKE THINGS EASIER TO READ:
# VIEW (at the top) -> WORD WRAP

# Import statements:
import csv

# Project outline and requirements:

# OUTLINE - The LMS will consist of the following classes and methods:

# 1. Create a Book class that has the following attributes (create a __init__ method)):
#    a. ISBN (int)
#    b. Title (string)
#    c. Author (string)
#    d. borrowed (boolean) - this should not be passed in as a parameter, it should be set to False by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES
class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = False

    def check_out(self):
        self.borrowed = True

    def check_in(self):
        self.borrowed = False


# Methods:
#    a. __str__ (returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>)
#    b. checkout - sets borrowed to True and returns a message that the book has been checked out
#    c. checkin - sets borrowed to False and returns a message that the book has been checked in
#    d. isBorrowed - returns True if the book is borrowed and False if the book is not borrowed


# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. Name (string)
#    c. ID (int)
#    d. borrowedBooks (list of books) - this should not be passed in as a parameter, it should be set to an empty list by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
#    b. borrow_book - adds the book to the borrowedBooks list, updates the isBorrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book as a parameter)
#    c. return_book - removes the book from the borrowedBooks list, updates the isBorrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book as a parameter)
class User:
    def __init__(self, name: str, member_id: int):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.borrowed:
            self.borrowed_books.append(book)
            book.check_out()
            return f"The book '{book.title}' has been checked out by {self.name}."
        else:
            return f"The book '{book.title}' is already checked out."

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.check_in()
            return f"The book '{book.title}' has been checked in by {self.name}."
        else:
            return f"The book '{book.title}' was not borrowed by {self.name}."


# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
#    b. add_book - adds a book to the books list (should take a book as a parameter)
#    c. add_user - adds a user to the users list (should take a user as a parameter)
#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowedBooks attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    def find_user(self, ID):
        for user in self.users:
            if user.ID == ID:
                return user
        return None    

    def export_books_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['ISBN', 'Title', 'Author', 'Borrowed']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for book in self.books:
                writer.writerow({'ISBN': book.isbn, 'Title': book.title, 'Author': book.author, 'Borrowed': book.borrowed})

    def export_users_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Name', 'ID', 'Borrowed Books']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.users:
                borrowed_books_titles = [book.title for book in user.borrowed_books]
                writer.writerow({'Name': user.name, 'ID': user.member_id, 'Borrowed Books': ', '.join(borrowed_books_titles)})


# 4. Create a menu that will allow users to:
#    a. Add books
#    b. Add users
#    c. Delete books
#    d. Delete users
#    g. Borrow books
#    h. Return books
#    i. Search books
#    j. Check if book is available
#    k. Search users
#    l. Export books to csv
#    m. Export users to csv
#    z. Exit

def display_menu():
    print("\n==== Library Menu ====")
    print("a. Add books")
    print("b. Add users")
    print("c. Delete books")
    print("d. Delete users")
    print("e. Borrow books")
    print("f. Return books")
    print("g. Search books")
    print("h. Check if book is available")
    print("i. Search users")
    print("j. Export books to csv")
    print("k. Export users to csv")
    print("z. Exit")


def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# RQUIREMENTS:
# 1. You should be doing error checking on all user input (make sure the user enters a valid ISBN, ID, etc.) and handle any errors appropriately (i.e. if the user enters an invalid ISBN, ask them to enter a valid ISBN)
# 2. You should be using try except blocks to handle any errors
# 3. You should be using the classes and methods outlined above with the exact names and parameters
# 4. You should be using the menu to call the appropriate methods
# 5. There is a Project3Tests.py file that will help you test your code. You should be able to run that file and pass all the tests.
#    Remember to run pytest use the following command in the terminal: pytest Project3Tests.py
# 6. The Project3Tests.py file is missing 2 tests. test_user_return and test_library_find_user. You will need to implement those tests and ensure they pass.
# 7. In your main method you should create a library object first to use for the rest of the program. You should not be creating a new library object every time you call a method. (Similar to the Store object in Lab 11)
# 8. In your main method you should be using a while loop to keep the program running until the user chooses to exit.

# IMPORTANT: You will only have 1 submission for this project so make sure you test your code thoroughly before submitting.

# You will be graded on the following:
# 1. Did you follow the project outline and requirements?
# 2. Does your code run without errors?
# 3. Did you use try except blocks to handle errors?
# 4. Did you use the classes and methods outlined above with the exact names and parameters?
# 5. Did you use the menu to call the appropriate methods?
# 6. Did you include docstrings for all classes and methods?
# 7. Did you include type hints for all methods?
# 8. Did your pytests for the test_user_return and test_library_find_user work?

def main():
    library = Library()  
    while True:
        display_menu()
        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            ISBN = get_int_input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            book = Book(title, author, ISBN)
            library.add_book(book)
            print(f"Book '{title}' added to the library.")

        elif choice == 'b':
            name = input("Enter user name: ")
            ID = get_int_input("Enter user ID: ")
            user = User(name, ID)
            library.add_user(user)
            print(f"User '{name}' added to the library.")

        elif choice == 'c':
            ISBN = get_int_input("Enter ISBN of the book to delete: ")
            book = library.find_book(ISBN)
            if book:
                library.books.remove(book)
                print(f"Book '{book.title}' deleted from the library.")
            else:
                print("Book not found.")

        elif choice == 'd':
            ID = get_int_input("Enter ID of the user to delete: ")
            user = library.find_user(ID)
            if user:
                library.users.remove(user)
                print(f"User '{user.name}' deleted from the library.")
            else:
                print("User not found.")

        elif choice == 'e':
            ID = get_int_input("Enter user ID: ")
            user = library.find_user(ID)
            if user:
                ISBN = get_int_input("Enter ISBN of the book to borrow: ")
                book = library.find_book(ISBN)
                if book:
                    result = user.borrow_book(book)
                    print(result)
                else:
                    print("Book not found.")
            else:
                print("User not found.")

        elif choice == 'f':
            ID = get_int_input("Enter user ID: ")
            user = library.find_user(ID)
            if user:
                ISBN = get_int_input("Enter ISBN of the book to return: ")
                book = library.find_book(ISBN)
                if book:
                    result = user.return_book(book)
                    print(result)
                else:
                    print("Book not found.")
            else:
                print("User not found.")

        elif choice == 'g':
            ISBN = get_int_input("Enter ISBN to search: ")
            book = library.find_book(ISBN)
            if book:
                print(f"Book found: {book}")
            else:
                print("Book not found.")

        elif choice == 'h':
            ISBN = get_int_input("Enter ISBN to check: ")
            book = library.find_book(ISBN)
            if book:
                if book.borrowed:
                    print(f"The book '{book.title}' is checked out.")
                else:
                    print(f"The book '{book.title}' is available.")
            else:
                print("Book not found.")

        elif choice == 'i':
            ID = get_int_input("Enter user ID to search: ")
            user = library.find_user(ID)
            if user:
                print(f"User found: {user}")
            else:
                print("User not found.")

        elif choice == 'j':
            filename = input("Enter CSV filename for books: ")
            library.export_books_to_csv(filename)
            print(f"Books exported to {filename}.")

        elif choice == 'k':
            filename = input("Enter CSV filename for users: ")
            library.export_users_to_csv(filename)
            print(f"Users exported to {filename}.")

        elif choice == 'z':
            print("Exiting the library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()