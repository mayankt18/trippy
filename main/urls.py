from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('sponsors/', views.sponsor_list, name='sponsor_list'),
]