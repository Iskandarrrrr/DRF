from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('media/', MediaView.as_view()),
    path('tags/', TagView.as_view()),
    path('posts/', PostView.as_view()),
    path('tagposts/', TagPostView.as_view()),
    path('authors/', AuthorsView.as_view()),
    path('authorposts/', AuthorPostsView.as_view()),
    path('tagauthors/', TagAuthorsView.as_view()),
    path('todayupdate/', TodayUpdateView.as_view()),
]


