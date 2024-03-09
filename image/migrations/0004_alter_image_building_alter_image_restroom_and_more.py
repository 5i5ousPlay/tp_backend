# Generated by Django 5.0.2 on 2024-03-09 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
        ('image', '0003_image_uploaded_by_image_uploaded_on'),
        ('restroom', '0002_alter_restroom_building'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='building.building'),
        ),
        migrations.AlterField(
            model_name='image',
            name='restroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='restroom.restroom'),
        ),
        migrations.AlterField(
            model_name='image',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='review.review'),
        ),
    ]