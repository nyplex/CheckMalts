# Generated by Django 4.0.3 on 2022-04-25 10:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0023_alter_cocktailssize_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='net_price',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10000)]),
        ),
    ]
