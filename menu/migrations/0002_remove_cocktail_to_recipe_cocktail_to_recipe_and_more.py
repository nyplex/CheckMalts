# Generated by Django 4.0.3 on 2022-04-10 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='to_recipe',
        ),
        migrations.AddField(
            model_name='cocktail',
            name='to_recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='menu.recipe'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='menu.ingredient'),
            preserve_default=False,
        ),
    ]
