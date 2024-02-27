# Generated by Django 5.0.2 on 2024-02-27 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building', '0001_initial'),
        ('restroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restroom',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restrooms', to='building.building'),
        ),
    ]
