# Generated by Django 3.1 on 2021-10-24 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20210916_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engine_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.CharField(default='', max_length=138)),
            ],
            options={
                'verbose_name_plural': 'Тип двигателя',
            },
        ),
        migrations.CreateModel(
            name='Engine_volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_volume', models.CharField(default='', max_length=138)),
            ],
            options={
                'verbose_name_plural': 'Объем двигателя',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission', models.CharField(default='', max_length=138)),
            ],
            options={
                'verbose_name_plural': 'Трансмиссия',
            },
        ),
        migrations.CreateModel(
            name='Type_drive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_drive', models.CharField(default='', max_length=138)),
            ],
            options={
                'verbose_name_plural': 'Привод',
            },
        ),
        migrations.AddField(
            model_name='automobiles',
            name='engine_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='about.engine_type'),
        ),
        migrations.AddField(
            model_name='automobiles',
            name='engine_volume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='about.engine_volume'),
        ),
        migrations.AddField(
            model_name='automobiles',
            name='transmission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='about.transmission'),
        ),
        migrations.AddField(
            model_name='automobiles',
            name='type_drive',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='about.type_drive'),
        ),
        migrations.CreateModel(
            name='Type_drive_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=138)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.languages')),
                ('type_drive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.type_drive')),
            ],
            options={
                'unique_together': {('type_drive', 'language')},
            },
        ),
        migrations.CreateModel(
            name='Transmission_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=138)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.languages')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.transmission')),
            ],
            options={
                'unique_together': {('transmission', 'language')},
            },
        ),
        migrations.CreateModel(
            name='Engine_volume_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=138)),
                ('engine_volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.engine_volume')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.languages')),
            ],
            options={
                'unique_together': {('engine_volume', 'language')},
            },
        ),
        migrations.CreateModel(
            name='Engine_type_description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=138)),
                ('engine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.engine_type')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.languages')),
            ],
            options={
                'unique_together': {('engine_type', 'language')},
            },
        ),
    ]
