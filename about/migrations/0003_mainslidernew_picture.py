# Generated by Django 3.1 on 2021-09-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_mainslidernew'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainslidernew',
            name='picture',
            field=models.ImageField(blank=True, upload_to='images/slider', verbose_name='picture_1920x1080'),
        ),
    ]
