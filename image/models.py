import uuid
import os
from django.db import models
from restroom.models import Restroom
from review.models import Review
from building.models import Building
from user.models import CustomUser as User
from core.utils.functions import get_image_upload_path


# Create your models here.
class Image(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    restroom = models.ForeignKey(Restroom, on_delete=models.CASCADE, null=True, related_name='images')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True, related_name='images')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, related_name='images')
    # image = models.ImageField(upload_to=get_image_upload_path, max_length=255)
    image = models.ImageField(upload_to='images/', max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True, null=True)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)

        super(Image, self).delete(*args, **kwargs)
