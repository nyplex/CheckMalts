# Generated by Django 4.0.3 on 2022-06-10 14:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0036_alter_cocktail_friendly_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='has_alcohol',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='net_price',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='cocktail',
            name='slug',
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
