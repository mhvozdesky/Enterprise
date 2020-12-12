# Generated by Django 3.1 on 2020-12-12 15:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_news_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.AddField(
            model_name='news',
            name='short_description',
            field=ckeditor.fields.RichTextField(default='', max_length=138),
        ),
        migrations.AddField(
            model_name='promotion',
            name='short_description',
            field=ckeditor.fields.RichTextField(default='', max_length=138),
        ),
        migrations.AlterField(
            model_name='automobiles',
            name='picture_770_340',
            field=models.ImageField(upload_to='images/automobiles', verbose_name='picture 770x340'),
        ),
        migrations.AlterField(
            model_name='automobiles',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='picture_1024_768',
            field=models.ImageField(upload_to='images/slider', verbose_name='picture 1024x768'),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='picture_1280_1024',
            field=models.ImageField(upload_to='images/slider', verbose_name='picture 1280x1024'),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='picture_1920_1080',
            field=models.ImageField(upload_to='images/slider', verbose_name='picture 1920x1080'),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='picture_2560_1080',
            field=models.ImageField(upload_to='images/slider', verbose_name='picture 2560x1080'),
        ),
        migrations.AlterField(
            model_name='news',
            name='picture_563_266',
            field=models.ImageField(default='images\\news1.jpg', upload_to='images/news_and_promotion', verbose_name='picture 563x266'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=54),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='picture_563_266',
            field=models.ImageField(default='images\\news1.jpg', upload_to='images/news_and_promotion', verbose_name='picture 563x266'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='text',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='title',
            field=models.CharField(max_length=54),
        ),
    ]
