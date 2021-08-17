from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('ru', views.index, name='index'),
    re_path(r'^old', views.index, name='index'),
    re_path(r'^[a-zA-Z]{2}/old', views.index, name='index'),
    
]