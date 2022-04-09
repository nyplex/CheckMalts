# Generated by Django 4.0.3 on 2022-04-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_email', models.EmailField(max_length=250)),
                ('booking_name', models.CharField(max_length=100)),
                ('booking_date', models.DateTimeField(max_length=50)),
                ('booking_time', models.CharField(choices=[('1400', '14:00'), ('1430', '14:30'), ('1500', '15:00'), ('1530', '15:30'), ('1600', '16:30'), ('1630', '16:30'), ('1700', '17:00'), ('1730', '17:30'), ('1800', '18:00'), ('1830', '18:30'), ('1900', '19:00'), ('1930', '19:30'), ('2000', '20:00'), ('2030', '20:30'), ('2100', '21:00'), ('2130', '21:30'), ('2200', '22:00'), ('2230', '22:30'), ('2300', '23:00')], max_length=10)),
                ('booking_size', models.CharField(choices=[('', 'Choose Size'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=10)),
            ],
        ),
    ]