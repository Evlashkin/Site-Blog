from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import F

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


class SinglePost(DetailView):
    model = Posts
    context_object_name = 'single'
    template_name = 'blog/single.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SinglePost, self).get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        query_set_tags = Posts.objects.get(slug=self.kwargs['slug']).tags.all()
        listtags = []
        for item in query_set_tags:
            tag = item.title
            listtags.append(tag)
        context['tags'] = listtags
        return context

