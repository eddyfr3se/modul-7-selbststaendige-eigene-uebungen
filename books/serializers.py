from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    pages = serializers.IntegerField(min_value=0)
    published_year = serializers.IntegerField(min_value=0)
    summary = serializers.CharField()
    isbn = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.pages = validated_data.get("pages", instance.pages)
        instance.published_year = validated_data.get(
            "published_year", instance.published_year
        )
        instance.summary = validated_data.get("summary", instance.summary)
        instance.isbn = validated_data.get("isbn", instance.isbn)
        instance.save()
        return instance
