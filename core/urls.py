from django.contrib.auth import views
from django.urls import path

from core.views import *

urlpatterns = [
    path('', frontpage, name='index'),
]