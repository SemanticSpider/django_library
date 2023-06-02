from django.shortcuts import render
from .models import Book, BookInstance, Author, Language, Genre
# Create your views here.

def index(request):
    """
    Function rendering home page
    """
    # Считаем книги и копии
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Считаем количество доступных копий
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_books':num_books, 'num_instances': num_instances, 'num_instances_available': num_instances_available,
            'num_authors': num_authors,
        }
    )
