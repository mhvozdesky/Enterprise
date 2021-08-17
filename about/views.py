import re
from django.shortcuts import render
from about.models import MainSlider, Automobiles, News, Promotion, Languages, News_description, Promotion_description, Automobiles_description
from local_languages import lang_file

def index(request):
    if len(re.findall(r'^/ru/', request.path)) > 0:
        lang = 'ru'#
        path_other_lang = request.path[3:] #switch to Ukrainian
        lang_id = 4
    else:
        lang = 'uk'
        path_other_lang = r'/ru' + request.path #switch to Russian
        lang_id = 3
    
    
    lang_dict = lang_file.lang_dict[lang_id]
        
    count_slides = MainSlider.objects.all().count()
    list_slides = MainSlider.objects.all()
    QuerySet_automobiles = Automobiles.objects.all()
    last_news = News.objects.all()[0]
    last_promotion = Promotion.objects.all()[0]
    
    title_news = ''
    shot_description_news = ''
    
    title_promotion = ''
    shot_description_promotion = ''   
    
    description_news = News_description.objects.filter(News = last_news.id, language = lang_id)
    description_promotions = Promotion_description.objects.filter(Promotion = last_promotion.id, language = lang_id)
    
    if len(description_news) > 0:
        title_news = description_news[0].title
        shot_description_news = description_news[0].short_description
        
    if len(description_promotions) > 0:
        title_promotion = description_promotions[0].title
        shot_description_promotion = description_promotions[0].short_description
        
    list_automobiles = []
    for auto in QuerySet_automobiles:
        local_dict_automobiles = {}
        local_dict_automobiles['url_auto'] = auto.picture_770_340
        querySet_Automobiles_description = Automobiles_description.objects.filter(Automobile = auto.id, language = lang_id)
        
        if len(querySet_Automobiles_description) > 0:
            local_dict_automobiles['title_auto'] = querySet_Automobiles_description[0].title
        else:
            local_dict_automobiles['title_auto'] = ''
            
        local_dict_automobiles['availability_hybrid'] = auto.availability_hybrid  
        local_dict_automobiles['price_starts'] = auto.price_starts
        
        list_automobiles.append(local_dict_automobiles)
    
    context = {
        #'pref': pref,
        'lang': lang,
        'lang_id': lang_id,
        'path_other_lang': path_other_lang,
        'count_slides': count_slides,
        'list_slides': list_slides,
        'list_automobiles': list_automobiles,
        'last_news': last_news,
        'last_promotion': last_promotion,
        'title_news': title_news,
        'shot_description_news': shot_description_news,
        'title_promotion': title_promotion,
        'shot_description_promotion': shot_description_promotion,
        'lang_dict': lang_dict,
        
    }
    
    if request.path == r'/old' or request.path == r'/ru/old':
        template = r'index\index_old.html'
    else:
        template = r'index\index.html'

    return render(request, template, context=context)
