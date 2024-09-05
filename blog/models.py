from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Media(models.Model):
    title = models.CharField(_('title'), max_length=255)
    file = models.FileField(_('File'), upload_to='media')

    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Medias')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(_('title'), max_length=255)
    order = models.IntegerField(_('Order'), default=0)


    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(_('Name'), max_length=120)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Post(models.Model):
    title = models.CharField(_('title'), max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    body = models.TextField(_('Body'))
    image = models.ManyToManyField(to=Media,  null=True, blank=True, verbose_name=_('Image'))
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name=_('Category'),
                                 related_name='posts')


    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'))




    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title


class TagPost(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name=_('Tag'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('Post'))

    class Meta:
        verbose_name = _('Tag Post')
        verbose_name_plural = _('Tag Posts')


    def __str__(self):
        return 'ManyToManyField'




class Authors(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    AuthorBio = models.TextField(_('Bio'), blank=True)
    social = models.CharField(_('Social'), max_length=255, blank=True)
    image = models.ImageField(_('Image'), upload_to='authors')

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return self.name

class AuthorPosts(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)
    description = models.TextField(_('Description'), blank=True)
    image = models.ImageField(_('Image'), upload_to='authors_image')
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, verbose_name='Author')

    class Meta:
        verbose_name = _('Authorpost')
        verbose_name_plural = _('Authorposts')

    def __str__(self):
        return self.title

class TagAuthors(models.Model):
    name = models.CharField(_('Title'), max_length=100)

    class Meta:
        verbose_name = _('Tagauthor')
        verbose_name_plural = _('Tagauthors')


class TodayUpdate(models.Model):
    quantity = models.IntegerField(_('Quantity'), default=0)
    title = models.CharField(_('Title'), max_length=150)

    class Meta:
        verbose_name = _('Today')
        verbose_name_plural = _('Today')


class CommentAndInfo(models.Model):
    author = models.ForeignKey(to=Authors, on_delete=models.CASCADE, verbose_name='Author')
    comment = models.TextField()
    personal_info = models.CharField(_('Personal Info'), max_length=210, blank=True)
    gmail = models.CharField(_('Gmail'), blank=True, max_length=210)

    class Meta:
        verbose_name = 'CommentInfo'
        verbose_name_plural = 'CommentsInfo'


class InfoEarn(models.Model):
    title = models.CharField(_('Title'), max_length=255)
    text = models.TextField()


    class Meta:
        verbose_name = 'InfoEarn'
        verbose_name_plural = 'InfoEarns'

