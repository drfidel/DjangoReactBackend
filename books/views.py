from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import BookAuthor, Book
from .bookSerializers import BookSerializer, BookAuthorSerializer

class BookAuthorView(ListCreateAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(BookAuthor, id=self.request.data.get('author_id'))
        return serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleBookAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer
        

class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(BookAuthor, id=self.request.data.get('author_id'))
        return serializer.save(author=author)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class SingleBookView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer