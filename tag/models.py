import uuid
from django.db import models
from restroom.models import Restroom
from user.models import CustomUser as User


# Create your models here.
class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='tags')
    name = models.CharField(max_length=255)
    restroom = models.ManyToManyField(Restroom, related_name='tags')

    def __str__(self):
        return self.name
