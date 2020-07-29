from django.urls import path
from .views import AuthorView, ArticleView

#app_name = 'articles'

#will help us reverse look up later
urlpatterns = [
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>', AuthorView.as_view()),
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
]
