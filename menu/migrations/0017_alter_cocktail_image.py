# Generated by Django 4.0.3 on 2022-04-19 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0016_alter_cocktail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='image',
            field=models.ImageField(blank=True, default='default.png', upload_to='products_images/'),
        ),
    ]
