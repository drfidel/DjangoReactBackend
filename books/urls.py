from django.urls import path
from .views import BookAuthorView, SingleBookAuthorView, BookView, SingleBookView

app_name = 'books'

#will help us reverse look up later
urlpatterns = [
    path('bookauthors/', BookAuthorView.as_view()),
    path('bookauthors/<int:pk>', SingleBookAuthorView.as_view()),
    path('books/', BookView.as_view()),
    path('books/<int:pk>', SingleBookView.as_view()),
]