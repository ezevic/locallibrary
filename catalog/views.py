import http
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView


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
class BookListView(ListView):
    model = Book

    # Si no pongo nada más, por defecto esta vista crea el queryset de todos los objetos de Book.
    # Si quiero hacer uno personalizado, puedo generar una funcion get_queryset()

    def get_queryset(self):
        return Book.objects.all()

    # Por defecto, el contexto que se envia al template es el query especificado en el model = Book.
    # Para especificar que quiero mandar en el context, hago lo siguiente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['algun_valor'] = 'esto es algo que se envia al template como context'
        return context

"""

class BookListView(ListView):
    model = Book
    paginate_by = 10


class BookDetailView(DetailView):
    model = Book


class AuthorListView(ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(DetailView):
    model = Author

"""
La manera larga de escribir la vista de clase ListView es la siguiente

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
"""


"""
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'home.html', context)
"""

"""
La manera de escribir la vista de clase BookDetailView como función es la siguiente

def book_detail_view(request, primary_key):
    try:
        book = Book.objects.get(pk=primary_key)
    except Book.DoesNotExist:
        raise Http404('book does not exist')
    return render(request, 'book-detail.html', context={'book': book})


Hay otra manera mas corta de hacerlo:

from django.shortcuts import get_object_or_404

def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'catalog/book_detail.html', context={'book': book})

        
"""
