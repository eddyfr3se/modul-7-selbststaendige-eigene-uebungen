from django.urls import path
from .views import book_detail, book_list

urlpatterns = [
    path("books/", book_list, name="book-list"),
    path("books/<int:pk>/", book_detail, name="book-detail"),
]
