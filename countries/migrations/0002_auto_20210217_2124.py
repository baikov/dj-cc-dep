# Generated by Django 3.0.12 on 2021-02-17 18:24

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='continent',
            field=models.CharField(choices=[('AF', 'Африка'), ('AS', 'Евразия (Азия)'), ('EU', 'Евразия (Европа)'), ('NA', 'Северная Америка'), ('SA', 'Южная Америка'), ('AU', 'Австралия'), ('NO', '')], default='NO', max_length=50, verbose_name='Континент'),
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Название')),
                ('date', models.DateField(blank=True, verbose_name='Дата утверждения')),
                ('proportion', models.CharField(blank=True, max_length=10, verbose_name='Пропорции')),
                ('colors', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('figure', models.CharField(blank=True, max_length=250, verbose_name='Фигура на флаге')),
                ('emoji', models.CharField(blank=True, max_length=20, verbose_name='Эмоджи')),
                ('short_description', models.TextField(blank=True, max_length=550, verbose_name='Краткое описание')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='countries.Country')),
            ],
        ),
    ]
