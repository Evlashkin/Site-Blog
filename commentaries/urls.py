from django.urls import path

from .views import *


urlpatterns = [
    path('', add_comment, name='add_comment'),
]

