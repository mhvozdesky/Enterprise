# Generated by Django 3.1 on 2021-01-29 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_remove_news_bubu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='title',
        ),
        migrations.AddField(
            model_name='title',
            name='news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='about.news'),
        ),
    ]
