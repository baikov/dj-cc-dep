# Generated by Django 3.0.12 on 2021-02-19 11:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20210217_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flag',
            name='colors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
    ]
