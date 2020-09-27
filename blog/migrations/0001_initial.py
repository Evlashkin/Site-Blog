# Generated by Django 3.1.1 on 2020-09-25 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование категории')),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Наименование тега')),
                ('slug', models.SlugField(max_length=500)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Наименование публикации')),
                ('slug', models.SlugField(max_length=200)),
                ('content', models.TextField(blank=True, verbose_name='Контент публикации')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d', verbose_name='Фото')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='blog.Tags')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]