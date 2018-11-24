from django.apps import AppConfig


class CartonConfig(AppConfig):
    name = 'carton'
    #https://stackoverflow.com/a/41614413
    def ready(self):
        from . import signals
