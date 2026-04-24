# 📚 Bookstore API

A RESTful API for managing books, authors, and categories built with Django and Django REST Framework.

## 🚀 Overview
This project is designed to manage a bookstore system with advanced API capabilities including filtering, searching, and optimized database queries.

## 🧰 Tech Stack
- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Django Filter

## ⚙️ Features

### 📖 Book Management
- Full CRUD operations for books
- Optimized queries using `select_related`
- Image upload support for book covers

### 👤 Author & Category Management
- Separate models for authors and categories
- Relationship handling using ForeignKey
- Clean admin interface for management

### 🔍 Advanced API Features
- Filtering by category and author
- Search functionality (`title`, `description`, `author`)
- Ordering by price and title

### 🔐 Permissions
- Read access for all users
- Write operations restricted (IsAuthenticatedOrReadOnly)

### 🧱 Serializer Design
- Nested serializers for read operations
- Separate `author_id` and `category_id` for write operations

### ⚡ Extra Features
- Custom admin panel configuration
- Data seeding script (`populate_books.py`)

## 📦 Project Structure
- apps/books
  - models
  - serializers
  - views
  - admin

## ⚙️ Installation

```bash
git clone https://github.com/t-zare-Programmer/bookstore-api.git
cd bookstore-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
