# Generated by Django 3.0.12 on 2021-02-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0011_auto_20210224_2342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flag',
            old_name='has_horizontal_stripes',
            new_name='is_horizontal_stripes',
        ),
        migrations.AddField(
            model_name='flag',
            name='is_animal',
            field=models.BooleanField(default=False, verbose_name='Животное'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_bird',
            field=models.BooleanField(default=False, verbose_name='Птица'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_circle',
            field=models.BooleanField(default=False, verbose_name='Круг'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_country_name',
            field=models.BooleanField(default=False, verbose_name='Название страны'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_crescent',
            field=models.BooleanField(default=False, verbose_name='Полумесяц'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_cross',
            field=models.BooleanField(default=False, verbose_name='Крест'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_crown',
            field=models.BooleanField(default=False, verbose_name='Корона'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_diagonal_stripes',
            field=models.BooleanField(default=False, verbose_name='Диагональные полосы'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_diamond',
            field=models.BooleanField(default=False, verbose_name='Ромб'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_emblem',
            field=models.BooleanField(default=False, verbose_name='Герб'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_motto',
            field=models.BooleanField(default=False, verbose_name='Девиз'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_plant',
            field=models.BooleanField(default=False, verbose_name='Растение'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_star',
            field=models.BooleanField(default=False, verbose_name='Звезда'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_sun',
            field=models.BooleanField(default=False, verbose_name='Солнце'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_triangle',
            field=models.BooleanField(default=False, verbose_name='Треугольник'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_vertical_stripes',
            field=models.BooleanField(default=False, verbose_name='Вертикальные полосы'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_weapon',
            field=models.BooleanField(default=False, verbose_name='Оружие'),
        ),
    ]
