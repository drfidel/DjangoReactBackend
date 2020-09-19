from rest_framework import serializers

from .models import Book, BookAuthor

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'bookTitle', 'description', 'book_poster' , 'published_date' , 'author_id')

    bookTitle = serializers.CharField(max_length=120)
    description = serializers.CharField()
    book_poster = serializers.ImageField()
    published_date = serializers.DateTimeField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.bookTitle = validated_data.get('bookTitle', instance.bookTitle)
        instance.description = validated_data.get('description', instance.description) 
        instance.book_poster = validated_data.get('book_poster', instance.book_poster) 
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.author_id = validated_data.get('author_id', instance.author_id)

        instance.save()
        return instance

class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuthor
        fields = ("name", "email")

    name = serializers.CharField(max_length=120)
    email = serializers.CharField()

    def create(self, validated_data):
        return BookAuthor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email) 

        instance.save()
        return instance