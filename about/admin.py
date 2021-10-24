from django.contrib import admin
from .models import MainSlider, Automobiles, News, Promotion, Languages, Title, News_description, Automobiles_description, Promotion_description, MainSliderNew, MainSlider_description_New
from .models import Engine_type, Engine_type_description, Engine_volume, Engine_volume_description, Transmission, Transmission_description, Type_drive, Type_drive_description

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
    
class MainSlider_description_NewInline(admin.TabularInline):
    model = MainSlider_description_New
    
class MainSliderNewAdmin(admin.ModelAdmin):
    inlines = [
        MainSlider_description_NewInline,
    ] 
    
class Engine_type_descriptionInline(admin.TabularInline):
    model = Engine_type_description
    
class Engine_typeAdmin(admin.ModelAdmin):
    inlines = [
        Engine_type_descriptionInline,
    ]  
    
class Engine_volume_descriptionInline(admin.TabularInline):
    model = Engine_volume_description
    
class Engine_volumeAdmin(admin.ModelAdmin):
    inlines = [
        Engine_volume_descriptionInline,
    ]  
    
class Transmission_descriptionInline(admin.TabularInline):
    model = Transmission_description
    
class TransmissionAdmin(admin.ModelAdmin):
    inlines = [
        Transmission_descriptionInline,
    ] 
    
class Type_drive_descriptionInline(admin.TabularInline):
    model = Type_drive_description
    
class Type_driveAdmin(admin.ModelAdmin):
    inlines = [
        Type_drive_descriptionInline,
    ]    
   

admin.site.register(MainSlider)
admin.site.register(MainSliderNew, MainSliderNewAdmin) 
admin.site.register(Automobiles, AutomobilesAdmin)
admin.site.register(News, NewsAdmin)
#admin.site.register(News)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Languages)
#admin.site.register(Title)
#admin.site.register(News_description)
#admin.site.register(Automobiles_description)
#admin.site.register(Promotion_description)
admin.site.register(Engine_type, Engine_typeAdmin)
admin.site.register(Engine_type_description)
admin.site.register(Engine_volume, Engine_volumeAdmin)
admin.site.register(Engine_volume_description)
admin.site.register(Transmission, TransmissionAdmin)
admin.site.register(Transmission_description)
admin.site.register(Type_drive, Type_driveAdmin)
admin.site.register(Type_drive_description)





    
