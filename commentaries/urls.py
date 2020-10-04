from django.urls import path

from .views import *


urlpatterns = {
    path('', Commmentaries.as_views(), name='Commentaries')
}

