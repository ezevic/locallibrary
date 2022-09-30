from django.contrib import admin

# Register your models here.

from .models import Genre, Book, BookInstance, Author


# Define the admin class

class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'date_of_birth', 'date_of_death')

    inlines = [BookInline]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            "fields": ('book', 'imprint', 'id')
        }),

        ('Availability', {
            "fields": ('status', 'due_back')
        }

        )
    )





# Register the admin class with the associated model
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)


# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
