from django.contrib import admin

# Register your models here.

from .models import Genre, Book, BookInstance, Author


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
