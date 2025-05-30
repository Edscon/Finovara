from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('dashboard_proba/', views.dashboard_proba, name='dashboard'),
]