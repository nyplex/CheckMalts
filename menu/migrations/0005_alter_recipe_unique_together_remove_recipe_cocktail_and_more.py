# Generated by Django 4.0.3 on 2022-04-11 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='recipe',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='cocktail',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.DeleteModel(
            name='Cocktail',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
