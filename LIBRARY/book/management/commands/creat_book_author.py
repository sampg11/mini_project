from django.core.management.base import BaseCommand
from faker import Faker
import random
from book.models import Book, Author


class Command(BaseCommand):
    help = "Generate realistic, foreign fake books and authors without duplicates."

    def add_arguments(self, parser):
        parser.add_argument(
            '--total',
            type=int,
            default=10,
            help='Number of books to create'
        )

    def handle(self, *args, **options):
        fake = Faker('en_US')
        total = options['total']

        genres = ["FIC", "SCI", "HIS"]
        created_books_count = 0

        self.stdout.write(self.style.WARNING("Generating fake data..."))

        while created_books_count < total:
            title_patterns = [
                f"The {fake.word().capitalize()} of {fake.city()}",
                f"{fake.job()} in {fake.country()}",
                f"The Last {fake.color_name().capitalize()}",
                f"Secrets of {fake.catch_phrase()}",
                f"A History of {fake.word().capitalize()}",
            ]
            book_title = random.choice(title_patterns)
            book, created = Book.objects.get_or_create(
                title=book_title,
                defaults={
                    'genre': random.choice(genres),
                    'publish_date': fake.date_between(start_date='-25y', end_date='today'),
                    'pages': random.randint(100, 900),
                    'price': random.randint(100000, 1000000),
                }
            )

            if not created:
                continue

            num_authors = random.randint(1, 3)
            authors_assigned = []

            for _ in range(num_authors):
                author, _ = Author.objects.get_or_create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name()
                )
                book.authors.add(author)
                authors_assigned.append(str(author))

            created_books_count += 1
            authors_str = ", ".join(authors_assigned)
            self.stdout.write(
                self.style.SUCCESS(f"[{created_books_count}/{total}] Created: '{book.title}' by ({authors_str})")
            )

        self.stdout.write(self.style.SUCCESS(f"\nSuccessfully created {total} unique books!"))