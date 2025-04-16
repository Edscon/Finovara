from django.urls import path
from . import views

urlpatterns = [
    path('', views.connection, name='connection'),
    path('dashboard_proba/', views.dashboard_proba, name='dashboard'),
]