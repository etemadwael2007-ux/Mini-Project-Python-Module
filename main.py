from models import User, Book
from library import LibraryManager

# إنشاء كائن من مدير المكتبة
app = LibraryManager()

# تجربة إضافة مستخدم جديد
print("--- Adding a new user ---")
app.add_user(user_id=1, name="Etemad", email="etemad@example.com")

# تجربة إضافة كتاب جديد
print("\n--- Adding a new book ---")
app.add_book(
    book_id=101,
    title="Python Programming Basics",
    author="John Doe",
    category="Programming",
    available_copies=3
)

# تجربة البحث عن كتاب
print("\n--- Searching for a book ---")
results = app.search_books("Programming")
for b in results:
    print(f"Found Book: {b.title} | Author: {b.author}")