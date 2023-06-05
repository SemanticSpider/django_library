from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Book, BookInstance, Author, Language, Genre
from django.views import generic
# Create your views here.

def index(request):
    """
    Function rendering home page
    """
    # Считаем книги и копии
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Numbers of visits to this view, as counted in the session variable

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Считаем количество доступных копий
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_books':num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available,
            'num_authors': num_authors, 'num_visits': num_visits
        }
    )

class BookListView(generic.ListView):
    model=Book
    paginate_by = 3

class BookDetailView(generic.DetailView):
    model=Book

class AuthorListView(generic.ListView):
    model=Author
    paginate_by= 3

class AuthorDetailView(generic.DetailView):
    model=Author



    

    