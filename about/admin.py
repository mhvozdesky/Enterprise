from django.contrib import admin
from .models import MainSlider, Automobiles, News, Promotion, Languages, Title, Short_description, Text

class TitleInline(admin.TabularInline):
    model = Title
    
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
    ] 

admin.site.register(MainSlider)
admin.site.register(Automobiles)
admin.site.register(News, NewsAdmin)
admin.site.register(Promotion)
admin.site.register(Languages)
admin.site.register(Title)
admin.site.register(Short_description)
admin.site.register(Text)




    
