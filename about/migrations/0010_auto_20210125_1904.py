# Generated by Django 3.1 on 2021-01-25 17:04

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_auto_20210108_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobiles_old',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('title_ru', models.CharField(default='', max_length=30)),
                ('picture_770_340', models.ImageField(upload_to='images/automobiles', verbose_name='picture 770x340')),
                ('availability_hybrid', models.BooleanField(default=False)),
                ('price_starts', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Automobiles_old',
            },
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='News_old',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=54)),
                ('title_ru', models.CharField(default='', max_length=54)),
                ('short_description', models.CharField(default='', max_length=138)),
                ('short_description_ru', models.CharField(default='', max_length=138)),
                ('publication_date', models.DateField(default=datetime.date.today)),
                ('picture_563_266', models.ImageField(default='images\\news1.jpg', upload_to='images/news_and_promotion', verbose_name='picture 563x266')),
                ('text', ckeditor.fields.RichTextField(default='')),
                ('text_ru', ckeditor.fields.RichTextField(default='')),
            ],
            options={
                'verbose_name_plural': 'News_old',
                'ordering': ['publication_date'],
            },
        ),
        migrations.CreateModel(
            name='Promotion_old',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=54)),
                ('title_ru', models.CharField(default='', max_length=54)),
                ('short_description', models.CharField(default='', max_length=138)),
                ('short_description_ru', models.CharField(default='', max_length=138)),
                ('publication_date', models.DateField(default=datetime.date.today)),
                ('picture_563_266', models.ImageField(default='images\\news1.jpg', upload_to='images/news_and_promotion', verbose_name='picture 563x266')),
                ('text', ckeditor.fields.RichTextField(default='')),
                ('text_ru', ckeditor.fields.RichTextField(default='')),
            ],
            options={
                'verbose_name_plural': 'Promotion_old',
                'ordering': ['publication_date'],
            },
        ),
        migrations.RemoveField(
            model_name='automobiles',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='short_description_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='short_description_ru',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='title_ru',
        ),
        migrations.CreateModel(
            name='Short_description',
            fields=[
                ('language', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='about.languages')),
                ('description', models.CharField(default='', max_length=138)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('language', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='about.languages')),
                ('text', ckeditor.fields.RichTextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('language', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='about.languages')),
                ('title_description', models.CharField(max_length=54)),
            ],
        ),
        migrations.AlterField(
            model_name='automobiles',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.title'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.short_description'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.text'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.title'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='short_description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.short_description'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.text'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.title'),
        ),
    ]
