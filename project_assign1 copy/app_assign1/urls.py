# app_assign1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('list/', views.pest_list, name='list'),
    path('details/<str:pest_id>/', views.pest_details, name='details'),
]
