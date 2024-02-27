# Generated by Django 5.0.2 on 2024-02-27 11:17

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rating', '0002_alter_rating_restroom'),
        ('restroom', '0002_alter_restroom_building'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('rating', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='rating.rating')),
                ('restroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='restroom.restroom')),
            ],
        ),
    ]