from django.apps import AppConfig
from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id","title","genre","publish_date","pages")
    search_fields = ("title",)
    list_filter = ("genre",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass