# 📚 Bookora

**A Library Management System — Built with Django**

A full-featured web application for managing books and authors, with user authentication, advanced search, a favorites system, and an admin panel.

---

## ✨ Features

- 🔐 **User Authentication** — register, log in, and log out
- 📖 **Book Management** — add, edit, delete, and view book details
- ✍️ **Author Management** — each book can have multiple authors (Many-to-Many relationship)
- 🔍 **Smart Search** — search books by title or author's first/last name
- ⭐ **Favorites List** — users can bookmark their favorite books
- 🔎 **Author Select Widget (Select2)** — live AJAX search widget for picking authors when adding a book
- 🛠️ **Django Admin Panel** — full management of books and authors from the admin dashboard
- 🎲 **Custom Management Commands** — generate fake test data and bulk-update book genres/prices
- 📄 **Pagination** — on the book list, search results, and favorites list

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.1 |
| Database | SQLite3 |
| Author selector widget | django-select2 |
| Fake data generation | Faker |

---

## 📁 Project Structure

```
LIBRARY/
├── LIBRARY/                # Core project settings (settings, urls, wsgi, asgi)
├── book/                   # Main application
│   ├── models.py           # Book and Author models
│   ├── views.py            # CBV/FBV views (list, detail, search, form, delete, ...)
│   ├── forms.py            # Registration form and book form
│   ├── admin.py            # Admin panel configuration
│   ├── urls.py              # App URL routes
│   └── management/commands/ # Custom commands (data generation, genre/price updates)
├── templates/home/          # HTML templates
├── db.sqlite3               # Database
└── manage.py
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+

### Installation

```bash
# 1. Go into the project folder
cd LIBRARY

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install required packages
pip install django django-select2 faker

# 4. Run migrations
python manage.py migrate

# 5. Create a superuser (to access the admin panel)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Then open your browser at:
👉 `http://127.0.0.1:8000/`

---

## 🧩 Custom Management Commands

To seed the database with test data:

```bash
# Generate random books and authors (default: 10)
python manage.py creat_book_author --total 30

# Update all books' genres from a predefined list
python manage.py update_genre

# Randomly update book prices (between $5 and $200)
python manage.py update_price
```

---

## 🗺️ Main Routes

| Route | Description |
|---|---|
| `/` | Homepage |
| `/register/` | User registration |
| `/login/` | User login |
| `/welcome/` | Welcome page (login required) |
| `/books/` | Book list |
| `/books/search/` | Book search |
| `/books/add/` | Add a new book |
| `/books/<id>/` | Book detail |
| `/books/<id>/edit/` | Edit a book |
| `/books/<id>/delete/` | Delete a book |
| `/books/<id>/favorite/` | Add/remove from favorites |
| `/admin/` | Django admin panel |

---

## 📌 Notes

- The project currently runs with `DEBUG = True` and is meant for development; before deploying to production, make sure to update `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` accordingly.
- Email sending uses the console backend (`console.EmailBackend`), meaning emails are only printed to the terminal.

---

## 📄 License

This project was built for learning and personal/educational purposes only.
