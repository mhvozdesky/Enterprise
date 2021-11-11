import re
import about.views as about_views
from django.shortcuts import render
from local_languages import lang_file
from about.models import Engine_type, Engine_type_description, Engine_volume, Engine_volume_description, Transmission, Transmission_description, Type_drive, Type_drive_description



def index(request):
    
    lang_info = about_views.get_lang_info(request)
    lang = lang_info[0]
    path_other_lang = lang_info[1]
    lang_id = lang_info[2]      
    
    lang_dict = lang_file.lang_dict[lang_id]
    
    list_automobiles = about_views.get_automobiles_info(lang_id)
    
    context = {
        'lang_dict': lang_dict,
        'path_other_lang': path_other_lang,
        'lang': lang,
        'list_automobiles': list_automobiles,
    }
    
    template = r'models/models.html'
    return render(request, template, context=context)
