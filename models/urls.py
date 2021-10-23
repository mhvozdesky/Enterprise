from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), 
    #re_path(r'^[a-zA-Z]{2}/', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns = [
    #path('', views.index, name='index'), 
    #path('ru/', views.index, name='index'),
    #re_path(r'^old/', views.index, name='index'),
    #re_path(r'^[a-zA-Z]{2}/old/', views.index, name='index'),
    
#]