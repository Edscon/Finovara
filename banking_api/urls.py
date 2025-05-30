from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('agreement_institution/<str:id_code>/', views.agreement_institution, name='agreement_institution'),


    path('dashboard_proba/', views.dashboard_proba, name='dashboard'),
]