from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    publish_date = models.DateField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    authors = models.ManyToManyField('Author', related_name='books')
    favorited_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,related_name='favorite_books',blank=True,)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Book {self.title}"


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Author {self.first_name} {self.last_name}"


