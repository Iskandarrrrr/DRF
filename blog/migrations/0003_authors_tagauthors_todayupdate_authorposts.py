# Generated by Django 4.2.15 on 2024-09-02 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tagpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('AuthorBio', models.TextField(blank=True, verbose_name='Bio')),
                ('social', models.CharField(blank=True, max_length=255, verbose_name='Social')),
                ('image', models.ImageField(upload_to='authors', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='TagAuthors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Tagauthor',
                'verbose_name_plural': 'Tagauthors',
            },
        ),
        migrations.CreateModel(
            name='TodayUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Today',
                'verbose_name_plural': 'Today',
            },
        ),
        migrations.CreateModel(
            name='AuthorPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('image', models.ImageField(upload_to='authors_image', verbose_name='Image')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.authors', verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Authorpost',
                'verbose_name_plural': 'Authorposts',
            },
        ),
    ]
