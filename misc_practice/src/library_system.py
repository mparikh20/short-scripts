'''
Implementation of a Library System using classes and methods.
'''

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None
        self.reservation_queue = []
      
class User():
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
  
class Library:
  
    def __init__(self):
        self.books = {}
        self.users = {}
        # initialize and track user IDs here
        self.user_id = 1
        

    def register_user(self, user: object):
        created_id = f'U{self.user_id}'
        user.user_id = created_id
        self.users[created_id] = user
        # update the ID for the next user
        self.user_id += 1
     
    def add_book(self, book):
        self.books[book.isbn] = book
    
    def find_book(self, isbn):
        return self.books.get(isbn, None)

    def borrow_book(self, isbn, user_id):
        book = self.find_book(isbn)
        # check if book exits
        if book is not None:
  
          # is it available?
          if book.available == True:
  
            # update status
            book.borrower = user_id
  
            # update the user profile
            self.users[user_id].borrowed_books.append(isbn)
            book.available = False
            return True
  
        return False

    def return_book(self, isbn, user_id):
  
        # get the book object
        book = self.find_book(isbn)
        # check if book exists and also that it's been borrowed
        if book is not None and book.borrower == user_id:
            self.users[user_id].borrowed_books.remove(isbn)
      
          # check if there's no one in the que for this book, return it.
          if len(book.reservation_queue) == 0:
        
              book.available = True
              book.borrower = None
          else:
        
              # otherwise, give it to the first user in the waitlist
              next_recipient = book.reservation_queue.pop(0)
              # remove the recipient, update the book's status, update User profile
              book.borrower = next_recipient
              self.users[next_recipient].borrowed_books.append(isbn)
              book.available = False
        
          return True
        return False


    def reserve_book(self, isbn, user_id):
  
        # check if book exists:
        book = self.find_book(isbn)
    
        # book does not exist
        if book is None:
          return False
  
        if book.available and self.borrow_book(isbn, user_id):
          return True

        if book.available == False and user_id not in book.reservation_queue:
          
          book.reservation_queue.append(user_id)
          return True
      
        return False
      
