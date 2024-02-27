import uuid
from django.db import models
from restroom.models import Restroom
from user.models import CustomUser as User
from rating.models import Rating


# Create your models here.
class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    restroom = models.ForeignKey(Restroom, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', null=True)
    content = models.TextField()
    rating = models.OneToOneField(Rating, on_delete=models.CASCADE, related_name='review', null=True)
