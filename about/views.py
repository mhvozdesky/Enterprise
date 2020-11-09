from django.shortcuts import render
from about.models import MainSlider, Automobiles, News, Promotion

def index(request):
    count_slides = MainSlider.objects.all().count()
    list_slides = MainSlider.objects.all()
    
    list_automobiles = Automobiles.objects.all()
    
    context = {
        'count_slides': count_slides,
        'list_slides': list_slides,
        'list_automobiles': list_automobiles,
    }
    
    return render(request, r'index\index.html')
