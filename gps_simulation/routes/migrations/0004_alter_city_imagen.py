# Generated by Django 5.1.1 on 2024-11-08 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_city_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/cities_images'),
        ),
    ]