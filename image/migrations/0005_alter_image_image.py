# Generated by Django 5.0.2 on 2024-03-26 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_alter_image_building_alter_image_restroom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=255, upload_to='images/'),
        ),
    ]