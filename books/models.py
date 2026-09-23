from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()
    published_year = models.PositiveIntegerField()
    summary = models.TextField()
    isbn = models.CharField(max_length=20)


# Create your models here.
