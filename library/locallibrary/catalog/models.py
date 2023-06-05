from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, non Fiction).
    """
    name = models.CharField(max_length=200, help_text='Entre a book genre (e.g. Science Fiction, French Poetry etc)')

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
    
        return self.name
    
class Book(models.Model):
    """
    Model representing a book (but not specific copy book)
    """

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter the brief description of the book")
    isbn = models.CharField('ISBN', max_length=200, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn>ISBN nubmers</a>">')
    genre = models.ManyToManyField(Genre, help_text="Sleect a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True,)

    def __str__(self):
        """
        String for representing the Models object
        """
        return self.title
    
    def get_absolute_url(self):

        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """
        Create the string of the genre
        """
        return ','.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'
    
class BookInstance(models.Model):
    """
    Model representing spercific copy of the book (that can be borrowed at the library)
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Avaliable'),
        ('r', 'Reversed'),
    )


    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
    
    def __str__(self):
        """
        Sting for representation bookinstance
        """
        return '%s %s' % (self.id, self.book.title)
    
class Author(models.Model):
    """
    Model representation authors
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    def get_absolute_url(self):
        """
        Returns the url to access a particular authir instance
        """

        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representation the Model object
        """
        return '%s, %s' % (self.last_name, self.first_name)
    class Meta:
        ordering = ['date_of_birth']
    
class Language(models.Model):
    """
    Model representation Author's language
    """
    name = models.CharField(max_length=200, help_text='Enter the book natural language (e.g. English, Spanish, French etc.)')

    def __str__(self):
        return self.name