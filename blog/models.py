from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование категории')
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'


class Tags(models.Model):
    title = models.CharField(max_length=50, verbose_name='Наименование тега')
    slug = models.SlugField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Posts(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование публикации')
    slug = models.SlugField(max_length=200)
    content = models.TextField(blank=True, verbose_name='Контент публикации')
    author = models.CharField(max_length=100, verbose_name='Автор')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name='Фото')
    created_at = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tags, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Публикация(ю)'
        verbose_name_plural = 'Публикации'

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})
