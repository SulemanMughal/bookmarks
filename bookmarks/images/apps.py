from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'
    verbose_name = 'Image bookmarks'

    def ready(self):
    # import signal handlers
        import images.signals
