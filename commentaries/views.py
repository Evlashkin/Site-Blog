from django.shortcuts import render
from django.views.generic import ListView, DetailView


class Commentaries(ListView):
    template_name = 'commentaries/commentaries.html'
