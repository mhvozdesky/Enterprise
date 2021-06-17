from django.contrib import admin
from .models import MainSlider, Automobiles, News, Promotion, Languages, Title, News_description, Automobiles_description, Promotion_description

class TitleInline(admin.TabularInline):
    model = News_description
    
class NewsAdmin(admin.ModelAdmin):
    inlines = [
        TitleInline,
    ] 
    
class Automobiles_descriptionInline(admin.TabularInline):
    model = Automobiles_description
    
class AutomobilesAdmin(admin.ModelAdmin):
    inlines = [
        Automobiles_descriptionInline,
    ] 
    
class Promotion_descriptionInline(admin.TabularInline):
    model = Promotion_description
    
class PromotionAdmin(admin.ModelAdmin):
    inlines = [
        Promotion_descriptionInline,
    ]     
    

admin.site.register(MainSlider)
admin.site.register(Automobiles, AutomobilesAdmin)
admin.site.register(News, NewsAdmin)
#admin.site.register(News)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Languages)
admin.site.register(Title)
admin.site.register(News_description)




    
