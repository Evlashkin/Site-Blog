from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class CommentModel(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Имя автора')
    content = models.TextField(verbose_name='Текст комментария')
    photo = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True, verbose_name='Аватар')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата добавления(обнавления) комментария')
    likes = models.IntegerField(verbose_name='Понравилось', default=0)
    post = models.ForeignKey('blog.Posts', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('commentaries', kwargs={"pk": self.pk})

    class MPTTMeta:
        order_insertion_by = ['name']
