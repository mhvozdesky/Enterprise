# Generated by Django 3.1 on 2020-11-09 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20201108_2123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-publication_date'], 'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='promotion',
            options={'ordering': ['-publication_date'], 'verbose_name_plural': 'Promotion'},
        ),
    ]