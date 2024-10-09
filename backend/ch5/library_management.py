class Library:
  _library_name = "Central Library"
  __total_books = 0
  available_books = {}


  def __init__(self, book_title, author) -> None:
    self.book_title = book_title
    self.author = author
    Library.__total_books += 1
    if self.book_title not in Library.available_books:
      Library.available_books[self.book_title] = {"author": self.author, "count": 1}
    else:
      Library.available_books[self.book_title]["count"] += 1


  @classmethod
  def get_total_books(cls):   # class method to access private attribute
    return f"Total books in {cls._library_name}: {cls.__total_books}"
  

  @staticmethod
  def library_info():
    print("Welcome to the Central Library. It's a place of knowledge and wisdom")


  def __del__(self):
    Library.__total_books -= 1
    print(f"{self.book_title} by {self.author} has been removed from the library.")


  def lend_book(self, book_title):
    if book_title in Library.available_books and Library.available_books[book_title]["count"] > 0:
      Library.available_books[book_title]["count"] -= 1
      print(f"{book_title} has been lent out.")
    else:
      print(f"{book_title} is not available right now.")

  
  def return_book(self, book_title):
    if book_title in Library.available_books:
      Library.available_books[book_title]["count"] += 1
      print(f"{book_title} has been returned.")
    else:
      print(f"{book_title} is not recognized by the system.")


  @staticmethod
  def display_available_books():
    print("Available books:")
    for title, info in Library.available_books.items():
      print(f"{title} by {info['author']} - Copies: {info['count']}")


