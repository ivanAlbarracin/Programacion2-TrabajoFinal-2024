# Generated by Django 5.1.1 on 2024-11-08 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_city_info_y_bodegas'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='cities_images/'),
        ),
    ]