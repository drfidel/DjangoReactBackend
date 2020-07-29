from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Article
from .serializers import ArticleSerializer, AuthorSerializer

class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response({"authors": serializer.data})
    
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
    
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('articles')

        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"Success": "Article {} updated successfully". format(article_saved.title)})
    
    def delete(self, request, pk):
        # get object with this pk
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message" : "Article with id '{}' has been deleted.".format(pk)},status=204)
