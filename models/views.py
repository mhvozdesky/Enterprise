import re
import about.views as about_views
from django.shortcuts import render
from local_languages import lang_file




def index(request):
    
    lang_info = about_views.get_lang_info(request)
    lang = lang_info[0]
    path_other_lang = lang_info[1]
    lang_id = lang_info[2]      
    
    lang_dict = lang_file.lang_dict[lang_id]
    
    context = {
        'lang_dict': lang_dict,
        'path_other_lang': path_other_lang,
        'lang': lang,
    }
    
    template = r'models/models.html'
    return render(request, template, context=context)
