from rest_framework.generics import ListAPIView
from .serializers import *

from .models import *


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class MediaView(ListAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializers


class TagView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class PostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class TagPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = TagPostSerializers

class AuthorsView(ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializers


class AuthorPostsView(ListAPIView):
    queryset = AuthorPosts.objects.all()
    serializer_class = AuthorPostsSerializers


class TagAuthorsView(ListAPIView):
    queryset = TagAuthors.objects.all()
    serializer_class = TagAuthorsSerializers


class TodayUpdateView(ListAPIView):
    queryset = TodayUpdate.objects.all()
    serializer_class = TodayUpdateSerializers