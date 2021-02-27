# Generated by Django 3.0.12 on 2021-02-26 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0012_auto_20210225_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='construction_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Дизайн флага'),
        ),
        migrations.AddField(
            model_name='flag',
            name='design_description',
            field=models.TextField(blank=True, verbose_name='Описание дизайна'),
        ),
    ]