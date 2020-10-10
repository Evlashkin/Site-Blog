from django.shortcuts import render, redirect

from .forms import *
from .models import CommentModel


def add_comment(request):
    qs = CommentModel.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_comment')
    else:
        form = CommentForm()
    return render(request, 'commentaries/comment_form.html', {'forms': form, 'commentaries': qs})

