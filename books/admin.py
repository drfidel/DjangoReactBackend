from django.contrib import admin

from .models import Book, BookAuthor

# Register your models here.

admin.site.register(Book)
admin.site.register(BookAuthor)