from django.forms import ModelForm

from .models import *


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['name', 'content', 'post']
