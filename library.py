#Library Management
#
#
#
import custom_exceptions

class Library:


    def __init__(self):
        self.books = {} # a dictionary with keys as unique book id's and values as a list of other attributes



    def register_book(self, book_id, title, author, status):
        """Adds a book to the Library."""

        """
        book_id
        title
        author
        status (A/I) #avalible or issused
        """

        if type(book_id) != int or type(title) != title or type(author) != author or status not in ['A', 'I']:
            raise ValueError

        if book_id in self.books.keys():
            self.books[book_id] = [title, author, status]

        else: #book_id already exists and cannot add the book
            raise custom_exceptions.BookIDExists



    def del_book(self, book_id):
        """If book is found in the library then
        deletes book from the library, else throws
        BookNotFound error."""

        if book_id in self.books.keys(): #book is in the library
            del self.books[book_id]

        else: #book does not exist in library
            raise custom_exceptions.BookNotFound



    def view_book_list(self):
        """Displays all the books avalible in the library."""

        for book in self.books:
            print(book)



    def issue_student_book(self, book_id):
        """Issues a book to a student."""

        if book_id in self.books.keys():
            self.books[book_id][-1] = 'I'

        else: #book not found
            raise custom_exceptions.BookNotFound



    def return_book(self):
        """Updates the system."""
        pass

