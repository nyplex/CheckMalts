# Generated by Django 4.0.3 on 2022-05-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_pending',
            field=models.BooleanField(default=True, verbose_name='Order pending?'),
        ),
    ]
