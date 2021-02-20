# Generated by Django 3.0.12 on 2021-02-19 12:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0003_auto_20210219_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flag',
            name='is_follow',
            field=models.BooleanField(default=True, verbose_name='follow'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_index',
            field=models.BooleanField(default=True, verbose_name='index'),
        ),
        migrations.AddField(
            model_name='flag',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
        migrations.AddField(
            model_name='flag',
            name='meta_description',
            field=models.TextField(blank=True, max_length=400, verbose_name='SEO Description'),
        ),
        migrations.AddField(
            model_name='flag',
            name='meta_h1',
            field=models.CharField(blank=True, max_length=250, verbose_name='SEO H1'),
        ),
        migrations.AddField(
            model_name='flag',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=250, verbose_name='SEO keywords'),
        ),
        migrations.AddField(
            model_name='flag',
            name='meta_title',
            field=models.CharField(blank=True, max_length=250, verbose_name='SEO Title'),
        ),
        migrations.AddField(
            model_name='flag',
            name='updated_date',
            field=models.DateField(auto_now=True),
        ),
    ]