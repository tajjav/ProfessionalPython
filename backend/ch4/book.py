class Book:
  total_books = 0

  def __init__(self, title, author) -> None:
    self.title = title
    self.author = author
    Book.total_books += 1


  def display_book_info(self):
    print(f"Book: {self.title} by {self.author}.")

  
  @classmethod
  def get_total_books(cls):
    return f"Total books: {cls.total_books}"
  

# instances of books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")


# attribute methods on instances
book1.display_book_info()
book2.display_book_info()

# no. of instances
print(Book.get_total_books())