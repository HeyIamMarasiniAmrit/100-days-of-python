class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = self.books.length

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are ")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Harry potter")
l1.addBook("sapines")
l1.addBook("Homo deusion")
l1.addBook("A.i book")
l1.showInfo()


l1.showInfo()