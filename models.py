from datetime import datetime
from enum import Enum
import re

class ReadStatus(Enum):
    BORROWED = "Borrowed"
    COMPLETED = "Completed"

class Category:
    def __init__(self, category_id: int, name: str):
        self.id = category_id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Book:
    def __init__(self, book_id: int, title: str, author: str, category: str, available_copies: int):
        self.id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available_copies = available_copies

    @property
    def available_copies(self) -> int:
        return self._available_copies

    @available_copies.setter
    def available_copies(self, value: int):
        if value < 0:
            raise ValueError("عدد النسخ المتاحة لا يمكن أن يكون بالسالب!")
        self._available_copies = value

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "available_copies": self.available_copies
        }

class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.id = user_id
        self.name = name
        self.email = email

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, value):
            raise ValueError("البريد الإلكتروني غير صحيح!")
        self._email = value

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

class Rating:
    def __init__(self, user_id: int, book_id: int, score: int, review: str = ""):
        self.user_id = user_id
        self.book_id = book_id
        self.score = score
        self.review = review

    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int):
        if not (1 <= value <= 10):
            raise ValueError("التقييم يجب أن يكون بين 1 و 10!")
        self._score = value

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "book_id": self.book_id,
            "score": self.score,
            "review": self.review
        }

class ReadingHistory:
    def __init__(self, user_id: int, book_id: int, date: str = None, status: ReadStatus = ReadStatus.BORROWED):
        self.user_id = user_id
        self.book_id = book_id
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = status if isinstance(status, ReadStatus) else ReadStatus(status)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "book_id": self.book_id,
            "date": self.date,
            "status": self.status.value
        }