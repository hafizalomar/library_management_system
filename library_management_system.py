class Library:
    book_list = []

    @classmethod
    def entry_book(self, book):
        self.book_list.append(book)

    @classmethod
    def view_all_books(self):
        print(f"\n\t\t\t---book in this library---")
        for book in self.book_list:
            book.view_book_info()
        print()

    @classmethod
    def find_book_id(self, book_id):
        for book in self.book_list:
            if book.get_book_id() == book_id:
                return book
        return None
        

class Book:
    def __init__(self, id, title, authour):
        self.__book_id = id
        self._title = title
        self._authour = authour
        self.__availability = "Available"

    def get_book_id(self):
        return self.__book_id

    def set_availability(self, availability):
        self.__availability = availability

    def view_book_info(self):
        print(f"ID: {self.__book_id}, Title: {self._title}, Author: {self._authour}, Availability: {self.__availability}")

    def borrow_book(self):
        if self.__availability == "Available":
            self.__availability = "Not Available"
            print(f"\nBook '{self._title}' borrowed successfully.\n")
        else:
            print(f"\nSorry, '{self._title}' is currently unavailable.\n")

    def return_book(self):
        if self.__availability == "Not Available":
            self.__availability = "Available"
            print(f"\nBook '{self._title}' returned successfully.\n")
        else:
            print(f"\nBook '{self._title}' was not borrowed.\n")

book1 = Book(101, "python programming", "John Doe")
book2 = Book(102, "data Science Essential", "Jone smith")
book3 = Book(103, "Machine Learning", "alan turing")
book4 = Book(104, "Intermediate English Grammear", "Raymond Murphy")
book5 = Book(105, "Basic for hacker", "OccopyTheWeb")

Library.entry_book(book1)
Library.entry_book(book2)
Library.entry_book(book3)
Library.entry_book(book4)
Library.entry_book(book5)
        

while(True):
    print("----Welcome to the Library----")
    print("1. View all Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    print()
    
    choice = input("Enter your choince: ")
    if choice == "1":
        Library.view_all_books()
    elif choice == "2":
        book_id = input("Enter book ID to borrow: ")
        book = Library.find_book_id(int(book_id))
        if book:
            book.borrow_book()
        else:
            print("Book id not found.")
    elif choice == "3":
        book_id = input("Enter book ID to return: ")
        book = Library.find_book_id(int(book_id))
        if book:
            book.return_book()
        else:
            print("Book id not found.")
    elif choice == "4":
        break
    else:
        print(f"\nThis option is not avalavle...\n")