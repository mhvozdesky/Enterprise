# Generated by Django 3.1 on 2021-11-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_auto_20211111_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobiles',
            name='price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]