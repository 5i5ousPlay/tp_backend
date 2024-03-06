import uuid
from django.db import models
from restroom.models import Restroom


# Create your models here.
class Rating(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    rating = models.FloatField()
    restroom = models.ForeignKey(Restroom, on_delete=models.CASCADE, related_name='ratings')
