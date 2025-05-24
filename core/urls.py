from django.contrib.auth import views
from django.urls import path, include

from core.views import *

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', frontpage, name='signup'),
    path('app/', include('banking_api.urls')),
]