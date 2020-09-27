from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Posts, Category, Tags


class Home(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


def index(request):
    return render(request, template_name='blog/index.html')


def category(request, slug):
    return render(request, template_name='blog/category.html')

def get_post(request, slug):
    return render (request, template_name='blog/category.html')
