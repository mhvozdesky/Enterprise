import re
from django.shortcuts import render
from local_languages import lang_file


def index(request):
    context = {}
    template = r'models_base.html'
    return render(request, template, context=context)
