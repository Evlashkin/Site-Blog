from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostByCategory.as_view(), name='category'),
    path('post/<str:slug>/', SinglePost.as_view(), name='single'),
    path('tags/<str:slug>/', PostByTags.as_view(), name='tags'),
]
