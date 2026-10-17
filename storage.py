import json
import os
from models import User, Book, Category, Rating, ReadingHistory, ReadStatus

class LibraryStorage:
    @staticmethod
    def save_data(filename: str, data_list):
        """حفظ قائمة من الكائنات في ملف JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([item.to_dict() for item in data_list], f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_users(filename: str = "users.json") -> list:
        """تحميل المستخدمين من ملف JSON"""
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User(item['id'], item['name'], item['email']) for item in data]

    @staticmethod
    def load_books(filename: str = "books.json") -> list:
        """تحميل الكتب من ملف JSON"""
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Book(item['id'], item['title'], item['author'], item['category'], item['available_copies']) for item in data]