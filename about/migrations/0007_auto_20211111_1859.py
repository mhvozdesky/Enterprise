# Generated by Django 3.1 on 2021-11-11 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0006_auto_20211029_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type_body',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_body', models.CharField(default='', max_length=138)),
            ],
            options={
                'verbose_name_plural': 'Тип кузова',
            },
        ),
        migrations.AddField(
            model_name='automobiles',
            name='type_body',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='about.type_body'),
        ),
        migrations.CreateModel(
            name='Type_body_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=138)),
                ('class_name', models.CharField(default='', max_length=138)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.languages')),
                ('type_body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.type_body')),
            ],
            options={
                'unique_together': {('type_body', 'language')},
            },
        ),
    ]