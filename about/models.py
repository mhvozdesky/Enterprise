import datetime
from django.db import models
from ckeditor.fields import RichTextField



class Languages(models.Model):
    language_name = models.CharField(max_length=200, default='')
    
    class Meta:
        verbose_name_plural = "Languages"    


class Short_description(models.Model):
    language = models.OneToOneField(Languages, on_delete = models.CASCADE, primary_key = True)
    description = models.CharField(default='', max_length=138)


class Text(models.Model):
    language = models.OneToOneField(Languages, on_delete = models.CASCADE, primary_key = True)
    text = RichTextField(default='')

    
class News(models.Model):
    #the model presents News
    
    #title = models.ForeignKey(Title, on_delete = models.CASCADE)
    publication_date = models.DateField(default=datetime.date.today)
    picture_563_266 = models.ImageField('picture 563x266', upload_to='images/news_and_promotion', default=r'images\news1.jpg') 
    
    class Meta:
        verbose_name_plural = "News"
        ordering = ['publication_date']  


class News_description(models.Model):
    
    News = models.ForeignKey(News, on_delete = models.CASCADE)
    title = models.CharField(default='', max_length=138)
    language = models.ForeignKey(Languages, on_delete = models.CASCADE)
    #short_description = models.ForeignKey(Short_description, on_delete = models.CASCADE)
    #text = models.ForeignKey(Text, on_delete = models.CASCADE)
    
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
        verbose_name_plural = "Main Slider"
 
    
class Automobiles(models.Model):
    #the model presents Automobiles
    
    title = models.ForeignKey(Title, on_delete = models.CASCADE)
    picture_770_340 = models.ImageField('picture 770x340', upload_to='images/automobiles')
    availability_hybrid = models.BooleanField(default=False)
    price_starts = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "Automobiles"    


#class News(models.Model):
    ##the model presents News
    
    ##title = models.ForeignKey(Title, on_delete = models.CASCADE)
    #short_description = models.ForeignKey(Short_description, on_delete = models.CASCADE)
    #publication_date = models.DateField(default=datetime.date.today)
    #picture_563_266 = models.ImageField('picture 563x266', upload_to='images/news_and_promotion', default=r'images\news1.jpg') 
    #text = models.ForeignKey(Text, on_delete = models.CASCADE)
    
    #class Meta:
        #verbose_name_plural = "News"
        #ordering = ['publication_date']
    
   

class Promotion(models.Model):
    #the model presents Automobiles
    
    title = models.ForeignKey(Title, on_delete = models.CASCADE)
    short_description = models.ForeignKey(Short_description, on_delete = models.CASCADE)
    publication_date = models.DateField(default=datetime.date.today)
    picture_563_266 = models.ImageField('picture 563x266', upload_to='images/news_and_promotion', default=r'images\news1.jpg')
    text = models.ForeignKey(Text, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Promotion"  
        ordering = ['publication_date']
        
  
        
