import os
from django.conf import settings


def get_image_upload_path(instance, filename):
    if instance.restroom:
        directory = os.path.join(settings.MEDIA_ROOT, 'restroom', str(instance.restroom.id))
    elif instance.review:
        directory = os.path.join(settings.MEDIA_ROOT, 'review', str(instance.review.id))
    elif instance.building:
        directory = os.path.join(settings.MEDIA_ROOT, 'building', str(instance.building.id))
    else:
        directory = settings.MEDIA_ROOT

    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    return os.path.join(directory, filename)
