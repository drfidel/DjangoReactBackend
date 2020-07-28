from rest_framework import serializers

from .models import Article, Author

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    created_date = serializers.DateTimeField()
    published_date = serializers.DateTimeField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    email = serializers.CharField()