# Generated by Django 3.0.12 on 2021-03-01 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0018_auto_20210301_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorderCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('border', models.PositiveIntegerField(help_text='в метрах', verbose_name='Протяженность границы')),
                ('border_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbour', to='countries.Country')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countries.Country')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='border_countries',
            field=models.ManyToManyField(related_name='_country_border_countries_+', through='countries.BorderCountry', to='countries.Country', verbose_name='Соседние страны'),
        ),
    ]
