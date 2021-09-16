import re
from django.shortcuts import render
from about.models import MainSlider, Automobiles, News, Promotion, Languages, News_description, Promotion_description, Automobiles_description, MainSliderNew, MainSlider_description_New
from local_languages import lang_file

def get_info_slider(QuerySet_slides_new, lang_id):
    list_info_slider = []
    for slider in QuerySet_slides_new:
        local_dict_slider = {}
        querySet_slider_description = MainSlider_description_New.objects.filter(Slider = slider.id, language = lang_id)
        local_dict_slider['picture'] = slider.picture.url
        local_dict_slider['slide_number'] = slider.slide_number
        local_dict_slider['title'] = ''
        local_dict_slider['short_description'] = ''
        local_dict_slider['text_button'] = ''
        
        if len(querySet_slider_description) > 0:
            local_dict_slider['title'] = querySet_slider_description[0].title
            local_dict_slider['short_description'] = querySet_slider_description[0].short_description
            local_dict_slider['text_button'] = querySet_slider_description[0].text_button       
        
        list_info_slider.append(local_dict_slider)
        
    return list_info_slider

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
    # new это адаптивная страница    
    count_slides = MainSlider.objects.all().count()
    count_slides_new = MainSliderNew.objects.all().count() # адаптивная страница
    list_slides = MainSlider.objects.all()
    QuerySet_slides_new = MainSliderNew.objects.all()
    QuerySet_automobiles = Automobiles.objects.all()
    last_news = News.objects.all()[0]
    last_promotion = Promotion.objects.all()[0]
    
    title_news = ''
    shot_description_news = ''
    
    title_promotion = ''
    shot_description_promotion = ''   
    
    description_news = News_description.objects.filter(News = last_news.id, language = lang_id)
    description_promotions = Promotion_description.objects.filter(Promotion = last_promotion.id, language = lang_id)
    
    # получим словарь для слайдера
    list_for_slider = get_info_slider(QuerySet_slides_new, lang_id) #получим список, в котором будут словари слайдера
    
    
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
        'list_for_slider': list_for_slider,
        
    }
    
    if request.path == r'/old/' or request.path == r'/ru/old/':
        template = r'index\index_old.html'
    else:
        template = r'index\index.html'

    return render(request, template, context=context)
