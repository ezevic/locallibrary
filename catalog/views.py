from django.shortcuts import render
from django.views.generic import View


from .models import Book, BookInstance, Author, Genre

# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Libros que contienen la palabra "the"

    book_include_the = Book.objects.filter(title__contains='the').count()



    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'book_include_the': book_include_the,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


"""
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'home.html', context)
"""
