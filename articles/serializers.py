from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    created_date = serializers.DateTimeField()
    published_date = serializers.DateTimeField()

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    email = serializers.CharField()