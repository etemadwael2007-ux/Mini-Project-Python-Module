from storage import LibraryStorage
from models import User, Book, Category, Rating, ReadingHistory, ReadStatus
from collections import Counter

class LibraryManager:
    def __init__(self):
        self.users = LibraryStorage.load_users()
        self.books = LibraryStorage.load_books()
        self.ratings = []
        self.history = []

    def add_user(self, user_id: int, name: str, email: str):
        # التحقق مما إذا كان المستخدم موجوداً مسبقاً لمنع التكرار
        for user in self.users:
            if user.user_id == user_id:
                print(f"User with ID {user_id} already exists!")
                return
                
        user = User(user_id, name, email)
        self.users.append(user)
        LibraryStorage.save_data("users.json", self.users)
        print(f"User {name} added successfully!")

    def add_book(self, book_id: int, title: str, author: str, category: str, available_copies: int):
        # التحقق مما إذا كان الكتاب موجوداً مسبقاً لمنع التكرار
        for book in self.books:
            if book.book_id == book_id:
                print(f"Book with ID {book_id} already exists!")
                return
                
        book = Book(book_id, title, author, category, available_copies)
        self.books.append(book)
        LibraryStorage.save_data("books.json", self.books)
        print(f"Book {title} added successfully!")

    def search_books(self, query: str):
        """البحث عن الكتب بالعنوان، المؤلف، أو التصنيف"""
        results = [
            b for b in self.books 
            if query.lower() in b.title.lower() 
            or query.lower() in b.author.lower() 
            or query.lower() in b.category.lower()
        ]
        return results