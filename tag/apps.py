from django.apps import AppConfig
from django.db.models.signals import post_migrate


class TagConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tag'

    def ready(self):
        from .signals import populate_default_tags
        post_migrate.connect(populate_default_tags, sender=self)
