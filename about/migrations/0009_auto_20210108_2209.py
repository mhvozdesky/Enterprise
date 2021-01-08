# Generated by Django 3.1 on 2021-01-08 20:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_auto_20201212_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobiles',
            name='title_ru',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='mainslider',
            name='picture_1024_768_ru',
            field=models.ImageField(default='', upload_to='images/slider', verbose_name='picture 1024x768 RU'),
        ),
        migrations.AddField(
            model_name='mainslider',
            name='picture_1280_1024_ru',
            field=models.ImageField(default='', upload_to='images/slider', verbose_name='picture 1280x1024 RU'),
        ),
        migrations.AddField(
            model_name='mainslider',
            name='picture_1920_1080_ru',
            field=models.ImageField(default='', upload_to='images/slider', verbose_name='picture 1920x1080 RU'),
        ),
        migrations.AddField(
            model_name='mainslider',
            name='picture_2560_1080_ru',
            field=models.ImageField(default='', upload_to='images/slider', verbose_name='picture 2560x1080 RU'),
        ),
        migrations.AddField(
            model_name='news',
            name='short_description_ru',
            field=models.CharField(default='', max_length=138),
        ),
        migrations.AddField(
            model_name='news',
            name='text_ru',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(default='', max_length=54),
        ),
        migrations.AddField(
            model_name='promotion',
            name='short_description_ru',
            field=models.CharField(default='', max_length=138),
        ),
        migrations.AddField(
            model_name='promotion',
            name='text_ru',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='promotion',
            name='title_ru',
            field=models.CharField(default='', max_length=54),
        ),
    ]
