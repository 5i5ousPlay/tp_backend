from .models import Tag
from django.conf import settings


def populate_default_tags(sender, **kwargs):
    DEFAULT_TAGS = settings.DEFAULT_TAGS
    for tag in DEFAULT_TAGS:
        new_tag, created = Tag.objects.get_or_create(name=tag)
