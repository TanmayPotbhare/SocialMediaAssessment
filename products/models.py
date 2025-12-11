from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    published_year = models.IntegerField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    isbn = models.CharField(max_length=20, unique=True, blank=True, null=True)  # New field for ISBN / Barcode

    def __str__(self):
        return self.title