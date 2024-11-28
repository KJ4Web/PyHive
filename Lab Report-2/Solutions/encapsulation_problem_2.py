class LibraryBook:
    def __init__(self, title, author, isbn):
        self.__isbn = isbn
        self._title = title
        self._author = author
        self._status = "available"
    def get_ISBN(self):
        return f"ISBN: {self.__isbn[:3]}-****-****-{self.__isbn[-3:]}"
    def borrow_book(self, borrower_name):
        if self._status == "available":
            self._status = "borrowed"
            print(f"{self._title} has been borrowed by {borrower_name}.")
        else:
            print(f"{self._title} is currently not available for borrowing.")
    def _display_basic_info(self):
        print(f"Title: {self._title}, Author: {self._author}")
class DigitalLibraryBook(LibraryBook):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format
    def display_info(self):
        self._display_basic_info()
        print(f"File Format: {self.file_format}")
book = LibraryBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
print(book.get_ISBN())
book.borrow_book("Alice")
digital_book = DigitalLibraryBook("Digital Fortress", "Dan Brown", "9780440240823", "PDF")
digital_book.display_info()