# Generated by Django 5.1.1 on 2024-11-08 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0004_alter_city_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='imagen',
            field=models.ImageField(null=True, upload_to='static/image'),
        ),
    ]
