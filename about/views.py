import re
from django.shortcuts import render
from about.models import MainSlider, Automobiles, News, Promotion, Languages

def index(request):
    if len(re.findall(r'^/ru', request.path)) > 0:
        lang = 'ru'#
        path_other_lang = request.path[3:] + r'/'
        pref = '_ru'
    else:
        lang = 'uk'
        path_other_lang = request.path + 'ru'
    
    
        
    count_slides = MainSlider.objects.all().count()
    list_slides = MainSlider.objects.all()
    list_automobiles = Automobiles.objects.all()
    last_news = News.objects.all()[0]
    last_promotion = Promotion.objects.all()[0]
    
    context = {
        'pref': pref,
        'lang': lang,
        'path_other_lang': path_other_lang,
        'count_slides': count_slides,
        'list_slides': list_slides,
        'list_automobiles': list_automobiles,
        'last_news': last_news,
        'last_promotion': last_promotion,
    }
    

    return render(request, r'index\index.html', context=context)
