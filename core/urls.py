from django.contrib.auth import views
from django.urls import path, include

from core.views import *

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('auth_manager/', auth_manager, name='auth_manager'),
    path('auth_manager/update_institutions/', update_institutions, name='update_institutions'),
    path('signup/', frontpage, name='signup'),
    path('app/', include('banking_api.urls')),
]