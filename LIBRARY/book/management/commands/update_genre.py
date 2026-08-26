import random
from django.core.management.base import BaseCommand
from book.models import Book


class Command(BaseCommand):
    help = 'Update book genres to match the target list'

    def handle(self, *args, **options):
        target_genres = [
            'Self Growth',
            'Science',
            'Technology',
            'Romance',
            'Mystery',
            'Fantasy',
        ]

        books = Book.objects.all()
        for book in books:
            book.genre = random.choice(target_genres)
            book.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully updated {books.count()} books with target genres.'
            )
        )