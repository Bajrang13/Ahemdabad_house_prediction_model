from django.urls import path
from . import views

urlpatterns = [
    path('ahmedabad/', views.ahmedabad, name='ahmedabad'),
]