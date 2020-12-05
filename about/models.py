import datetime
from django.db import models
from ckeditor.fields import RichTextField


class MainSlider(models.Model):
    #the model presents the main slider
    
    slide_number = models.IntegerField()
    picture_1920_1080 = models.ImageField(upload_to='images/slider')
    picture_1024_768 = models.ImageField(upload_to='images/slider')
    picture_1280_1024 = models.ImageField(upload_to='images/slider')
    picture_2560_1080 = models.ImageField(upload_to='images/slider')
    
    class Meta:
        verbose_name_plural = "Main Slider"
    
class Automobiles(models.Model):
    #the model presents Automobiles
    
    title = models.CharField(max_length=200)
    picture_770_340 = models.ImageField(upload_to='images/automobiles')
    availability_hybrid = models.BooleanField(default=False)
    price_starts = models.CharField(max_length=20)
    
    class Meta:
        verbose_name_plural = "Automobiles"    

class News(models.Model):
    #the model presents News
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    publication_date = models.DateField(default=datetime.date.today)
    picture_563_266 = models.ImageField(upload_to='images/news_and_promotion', default=r'images\news1.jpg') 
    content = RichTextField(null=True)
    
    class Meta:
        verbose_name_plural = "News"
        ordering = ['publication_date']

class Promotion(models.Model):
    #the model presents Automobiles
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    publication_date = models.DateField(default=datetime.date.today)
    picture_563_266 = models.ImageField(upload_to='images/news_and_promotion', default=r'images\news1.jpg')
    
    class Meta:
        verbose_name_plural = "Promotion"  
        ordering = ['publication_date']