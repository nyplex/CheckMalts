# Generated by Django 4.0.3 on 2022-04-17 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0012_remove_subcategory_category_category_sub_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='sub_category',
            new_name='sub_categories',
        ),
    ]