# Generated by Django 3.0.12 on 2021-02-22 22:02

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_auto_20210219_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_group', models.CharField(choices=[('red', 'Красный'), ('orange', 'Оранжевый'), ('yellow', 'Желтый'), ('green', 'Зеленый'), ('blue', 'Синий'), ('purple', 'Фиолетовый'), ('black', 'Черный'), ('brown', 'Коричневый'), ('maroon', 'Бордовый'), ('pink', 'Розовый'), ('white', 'Белый'), ('NO', '')], default='NO', max_length=50, verbose_name='Группа цветов')),
                ('hex', models.CharField(blank=True, max_length=7, unique=True, verbose_name='HEX')),
                ('rgb', django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, size=3, verbose_name='RGB')),
                ('cmyk', django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), blank=True, size=4, verbose_name='CMYK')),
                ('pantone', models.CharField(blank=True, max_length=100, verbose_name='Pantone')),
            ],
        ),
        migrations.RemoveField(
            model_name='flag',
            name='colors',
        ),
        migrations.AddField(
            model_name='flag',
            name='colors',
            field=models.ManyToManyField(blank=True, related_name='colors', to='countries.Color', verbose_name='Цвета'),
        ),
    ]
