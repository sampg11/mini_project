import random
from django.core.management.base import BaseCommand
from book.models import Book

class Command(BaseCommand):
    help = "Update book prices to USD with max 3 integer digits and 2 decimals."

    def handle(self, *args, **options):
        books = Book.objects.all()
        total_books = books.count()

        if total_books == 0:
            self.stdout.write(self.style.WARNING("Fair"))
            return

        for book in books:
            book.price = round(random.uniform(5.00, 200.99), 2)


        Book.objects.bulk_update(books, ['price'])

        self.stdout.write(
            self.style.SUCCESS(f"{total_books} update !")
        )