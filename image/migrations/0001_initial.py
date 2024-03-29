# Generated by Django 5.0.2 on 2024-03-09 08:26

import core.utils.functions
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('building', '0001_initial'),
        ('restroom', '0002_alter_restroom_building'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=core.utils.functions.get_image_upload_path)),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='building.building')),
                ('restroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restroom.restroom')),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.review')),
            ],
        ),
    ]
