from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Author, Article
from .serializers import ArticleSerializer, AuthorSerializer

class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
<<<<<<< HEAD
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SingleAuthorView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
        

class ArticleView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class SingleArticleView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
=======
    def post(self, request):
        author = request.data.get('article')

        #create article form above data
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response({"Success": "Author '{}' created successfully".format(author_saved.name)})

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        articles = request.data.get('articles')

        #create article form above data
        serializer = ArticleSerializer(data=articles)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"Success": "Article '{}' created successfully".format(article_saved.title)})
>>>>>>> parent of 6a7fc80... corrected git, completed CRUD
