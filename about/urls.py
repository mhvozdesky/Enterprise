from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('ru', views.index, name='index'),
    #path('ru', RedirectView.as_view(url='', permanent=True)),
]