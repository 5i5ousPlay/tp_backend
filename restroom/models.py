import uuid
from django.db import models
from building.models import Building


# Create your models here.
class Restroom(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='restrooms')
