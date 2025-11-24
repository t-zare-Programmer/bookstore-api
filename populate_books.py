import os
import django

# تنظیم مسیر پروژه و محیط Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookStoreAPI.settings')
django.setup()

from apps.books.models import Category, Author, Book

# ================== Categories ==================
categories_data = [
    {"name": "Fantasy", "description": "داستان‌های فانتزی و خیال‌پردازی", "slug": "fantasy"},
    {"name": "Technology", "description": "کتاب‌های فناوری و IT", "slug": "technology"},
    {"name": "Biography", "description": "زندگینامه افراد مشهور", "slug": "biography"},
    {"name": "Art", "description": "هنر و طراحی", "slug": "art"},
]

for cat_data in categories_data:
    Category.objects.get_or_create(**cat_data)

# ================== Authors ==================
authors_data = [
    {"first_name": "Michael", "last_name": "Johnson", "email": "michael@example.com",
     "phone_number": "09121112222", "birth_date": "1975-03-10", "website": "https://michaeljohnson.com"},
    {"first_name": "Sarah", "last_name": "Williams", "email": "sarah@example.com",
     "phone_number": "09123334455", "birth_date": "1985-07-20", "website": "https://sarahwilliams.com"},
    {"first_name": "David", "last_name": "Brown", "email": "david@example.com",
     "phone_number": "09124445566", "birth_date": "1990-01-15", "website": "https://davidbrown.com"},
]

for author_data in authors_data:
    Author.objects.get_or_create(**author_data)

# ================== Books ==================
books_data = [
    {"title": "Fantasy World", "author": Author.objects.get(first_name="Michael", last_name="Johnson"),
     "category": Category.objects.get(name="Fantasy"), "price": 189.99, "stock": 8,
     "isbn": "9781111111111", "description": "داستان‌های فانتزی جذاب"},

    {"title": "Modern Tech", "author": Author.objects.get(first_name="Sarah", last_name="Williams"),
     "category": Category.objects.get(name="Technology"), "price": 299.50, "stock": 5,
     "isbn": "9782222222222", "description": "فناوری و برنامه‌نویسی مدرن"},

    {"title": "Life of Great People", "author": Author.objects.get(first_name="David", last_name="Brown"),
     "category": Category.objects.get(name="Biography"), "price": 159.00, "stock": 10,
     "isbn": "9783333333333", "description": "زندگینامه افراد مشهور"},

    {"title": "Art & Creativity", "author": Author.objects.get(first_name="Sarah", last_name="Williams"),
     "category": Category.objects.get(name="Art"), "price": 129.99, "stock": 7,
     "isbn": "9784444444444", "description": "کتابی درباره هنر و خلاقیت"},
]

for book_data in books_data:
    Book.objects.get_or_create(**book_data)

print("تمام رکوردهای نمونه با موفقیت وارد شدند!")
