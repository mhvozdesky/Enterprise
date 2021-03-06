# Generated by Django 3.1 on 2021-06-17 15:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0017_auto_20210616_1851'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobiles_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=138)),
            ],
            options={
                'verbose_name_plural': 'Automobiles_description',
            },
        ),
        migrations.CreateModel(
            name='Promotion_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=138)),
                ('short_description', models.CharField(default='', max_length=138)),
                ('text', ckeditor.fields.RichTextField(default='')),
            ],
            options={
                'verbose_name_plural': 'Promotion_description',
            },
        ),
        migrations.RemoveField(
            model_name='text',
            name='language',
        ),
        migrations.RemoveField(
            model_name='automobiles',
            name='title',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='text',
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='title',
        ),
        migrations.AddField(
            model_name='news_description',
            name='short_description',
            field=models.CharField(default='', max_length=138),
        ),
        migrations.AddField(
            model_name='news_description',
            name='text',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.DeleteModel(
            name='Short_description',
        ),
        migrations.DeleteModel(
            name='Text',
        ),
        migrations.AddField(
            model_name='promotion_description',
            name='Promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.promotion'),
        ),
        migrations.AddField(
            model_name='promotion_description',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.languages'),
        ),
        migrations.AddField(
            model_name='automobiles_description',
            name='Automobile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.automobiles'),
        ),
        migrations.AddField(
            model_name='automobiles_description',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.languages'),
        ),
        migrations.AlterUniqueTogether(
            name='promotion_description',
            unique_together={('Promotion', 'language')},
        ),
        migrations.AlterUniqueTogether(
            name='automobiles_description',
            unique_together={('Automobile', 'language')},
        ),
    ]
