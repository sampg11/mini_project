from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path

from book.views import homepage, RegisterPageView, BookCreateView, welcom_view, BookListView, BookSearchView, \
    BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', homepage, name='homepage'),
    path('welcome/', welcom_view, name='welcom'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name="home/login.html"), name='login'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/search/', BookSearchView.as_view(), name='book_search'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/', BookListView.as_view(), name='book_list'),
]