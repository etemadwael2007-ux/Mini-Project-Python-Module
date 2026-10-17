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
        user = User(user_id, name, email)
        self.users.append(user)
        LibraryStorage.save_data("users.json", self.users)
        print(f"تم إضافة المستخدم {name} بنجاح!")

    def add_book(self, book_id: int, title: str, author: str, category: str, available_copies: int):
        book = Book(book_id, title, author, category, available_copies)
        self.books.append(book)
        LibraryStorage.save_data("books.json", self.books)
        print(f"تم إضافة الكتاب {title} بنجاح!")

    def search_books(self, query: str):
        """البحث عن الكتب بالعنوان، المؤلف، أو التصنيف"""
        results = [
            b for b in self.books 
            if query.lower() in b.title.lower() 
            or query.lower() in b.author.lower() 
            or query.lower() in b.category.lower()
        ]
        return results