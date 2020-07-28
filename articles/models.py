from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey('Author', related_name='articles',on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()
        self.delete()
    
    def __str__(self):
        return self.title