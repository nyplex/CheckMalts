# Generated by Django 4.0.3 on 2022-06-08 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0031_alter_recipe_unique_together_remove_recipe_cocktail_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='net_price',
        ),
    ]
