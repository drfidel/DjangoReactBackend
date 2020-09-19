from django.db import models
from django.utils import timezone

# Create your models here.
class BookAuthor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey('BookAuthor', related_name='books',on_delete=models.CASCADE)
    bookTitle = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    book_poster = models.ImageField(upload_to='images/', null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()
        self.delete()
    
    def __str__(self):
        return self.bookTitle