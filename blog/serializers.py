from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TagPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = TagPost
        fields = '__all__'


class AuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = '__all__'


class AuthorPostsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthorPosts
        fields = '__all__'

class TagAuthorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TagAuthors
        fields = '__all__'


class TodayUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodayUpdate
        fields = '__all__'