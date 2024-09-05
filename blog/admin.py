from django.contrib import admin
from .models import *



@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    pass

@admin.register(AuthorPosts)
class AuthorPostsAdmin(admin.ModelAdmin):
    pass


@admin.register(TagAuthors)
class TagAuthorsAdmin(admin.ModelAdmin):
    pass


@admin.register(TodayUpdate)
class TodayUpdateAdmin(admin.ModelAdmin):
    pass

@admin.register(CommentAndInfo)
class CommentAndInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(InfoEarn)
class InfoEarnAdmin(admin.ModelAdmin):
    pass