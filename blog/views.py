from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Posts, Category, Tags


class Home(ListView):
    model = Posts
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


class PostByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        cat = Category.objects.get(slug=self.kwargs['slug'])
        return Posts.objects.filter(category=cat)


def get_post(request, slug):
    return render(request, template_name='blog/category.html')
