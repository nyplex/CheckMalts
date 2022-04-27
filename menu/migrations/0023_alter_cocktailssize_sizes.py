# Generated by Django 4.0.3 on 2022-04-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0022_cocktail_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktailssize',
            name='sizes',
            field=models.CharField(blank=True, choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large'), ('simple', 'simple'), ('double', 'double'), ('triple', 'triple')], max_length=10, null=True),
        ),
    ]