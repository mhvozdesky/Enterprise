import re
import about.views as about_views
from django.shortcuts import render
from local_languages import lang_file
from about.models import Engine_type, Engine_type_description, Engine_volume, Engine_volume_description, Transmission, Transmission_description, Type_drive, Type_drive_description
from about.models import Type_body, Type_body_description

dict_param = {
    'p_1': 'price',
    'p_2': 'type_body_id',
    'p_3': 'engine_type_id',
    'p_4': 'engine_volume_id',
    'p_5': 'transmission_id',
    'p_6': 'type_drive_id',    
}

dict_price = {
    '1': {'price__lte': 500000},
    '2': {'price__gte': 500000, 'price__lte': 1000000},
    '3': {'price__gte': 1000000, 'price__lte': 1500000},
    '4': {'price__gte': 1500000, 'price__lte': 2000000},
    '5': {'price__gte': 2000000},
}


def index(request):
    
    lang_info = about_views.get_lang_info(request)
    lang = lang_info[0]
    path_other_lang = lang_info[1]
    lang_id = lang_info[2]      
    
    lang_dict = lang_file.lang_dict[lang_id]
    
    list_automobiles = about_views.get_automobiles_info(lang_id, *(dict_param, dict_price, request.GET))
    
    context = {
        'lang_dict': lang_dict,
        'path_other_lang': path_other_lang,
        'lang': lang,
        'list_automobiles': list_automobiles,
    }
    
    template = r'models/models.html'
    return render(request, template, context=context)
