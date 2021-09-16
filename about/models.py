import datetime
from django.db import models
from ckeditor.fields import RichTextField



class Languages(models.Model):
    language_name = models.CharField(max_length=200, default='')
    
    def __str__(self):        
        return  self.language_name
    
    class Meta:
        verbose_name_plural = "Языки"    

  
class News(models.Model):
    #the model presents News
    
    #title = models.ForeignKey(Title, on_delete = models.CASCADE)
    publication_date = models.DateField(default=datetime.date.today)
    picture_563_266 = models.ImageField('picture 563x266', upload_to='images/news_and_promotion', default=r'images\news1.jpg') 
    
    def __str__(self): 
        
        news_description_objects = News_description.objects.filter(News = self, language = 4)
        return  news_description_objects[0].title    
    
    class Meta:
        verbose_name_plural = "Новости"
        ordering = ['-publication_date']  


class News_description(models.Model):
    
    News = models.ForeignKey(News, on_delete = models.CASCADE)
    title = models.CharField(default='', max_length=138)
    language = models.ForeignKey(Languages, on_delete = models.CASCADE)
    short_description = models.CharField(default='', max_length=138)
    text = RichTextField(default='')
    
    class Meta:
        verbose_name_plural = "News_description" 
        unique_together = ('News', 'language',)

        
class Title(models.Model):
    language = models.OneToOneField(Languages, on_delete = models.CASCADE, primary_key = True)
    title_description = models.CharField(max_length=54)
    news = models.ForeignKey(News, on_delete = models.CASCADE, default=1)        


class MainSlider(models.Model):
    #the model presents the main slider
    
    slide_number = models.IntegerField()
    picture_1920_1080 = models.ImageField('picture 1920x1080', upload_to='images/slider')
    picture_1024_768 = models.ImageField('picture 1024x768', upload_to='images/slider')
    picture_1280_1024 = models.ImageField('picture 1280x1024', upload_to='images/slider')
    picture_2560_1080 = models.ImageField('picture 2560x1080', upload_to='images/slider')
    
    picture_1920_1080_ru = models.ImageField('picture 1920x1080 RU', upload_to='images/slider', default='')
    picture_1024_768_ru = models.ImageField('picture 1024x768 RU', upload_to='images/slider', default='')
    picture_1280_1024_ru = models.ImageField('picture 1280x1024 RU', upload_to='images/slider', default='')
    picture_2560_1080_ru = models.ImageField('picture 2560x1080 RU', upload_to='images/slider', default='') 
    

    class Meta:
        verbose_name_plural = "Слайдер на главной странице старый"
        
class MainSliderNew(models.Model):
    #the model presents the main slider
    
    slide_number = models.IntegerField()
    picture = models.ImageField('picture_1920x1080', upload_to='images/slider', blank=True)
    
    class Meta:
        verbose_name_plural = "Слайдер на главной странице"    

class MainSlider_description_New(models.Model):
    
    Slider = models.ForeignKey(MainSliderNew, on_delete = models.CASCADE)
    title = models.CharField(default='', max_length=138)
    language = models.ForeignKey(Languages, on_delete = models.CASCADE)
    short_description = models.CharField(default='', max_length=138)
    text_button = models.CharField(default='', max_length=138)
    
    class Meta:
        verbose_name_plural = "MainSlider_description" 
        unique_together = ('Slider', 'language',) 
 

 
    
class Automobiles(models.Model):
    #the model presents Automobiles
    
    picture_770_340 = models.ImageField('picture 770x340', upload_to='images/automobiles')
    availability_hybrid = models.BooleanField(default=False)
    price_starts = models.CharField(max_length=20)
    
    def __str__(self):
        querySet_auto = Automobiles_description.objects.filter(Automobile = self.id, language = 4) 
        auto = querySet_auto[0]
        
        return  'Автомобиль ' + auto.title
    
    class Meta:
        verbose_name_plural = "Автомобили" 
        
class Automobiles_description(models.Model):
    
    Automobile = models.ForeignKey(Automobiles, on_delete = models.CASCADE)
    title = models.CharField(default='', max_length=138)
    language = models.ForeignKey(Languages, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Automobiles_description" 
        unique_together = ('Automobile', 'language',)         



class Promotion(models.Model):
    #the model presents Automobiles
    
    publication_date = models.DateField(default=datetime.date.today)
    picture_563_266 = models.ImageField('picture 563x266', upload_to='images/news_and_promotion', default=r'images\news1.jpg')
    
    def __str__(self): 
        
        promotion_description_objects = Promotion_description.objects.filter(Promotion = self, language = 4)
        return  promotion_description_objects[0].title      
    
    class Meta:
        verbose_name_plural = "Акции"  
        ordering = ['publication_date']
        
class Promotion_description(models.Model):
    
    Promotion = models.ForeignKey(Promotion, on_delete = models.CASCADE)
    title = models.CharField(default='', max_length=138)
    language = models.ForeignKey(Languages, on_delete = models.CASCADE)
    short_description = models.CharField(default='', max_length=138)
    text = RichTextField(default='')
    
    class Meta:
        verbose_name_plural = "Promotion_description" 
        unique_together = ('Promotion', 'language',)        
        
  
        
