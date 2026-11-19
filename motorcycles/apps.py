from django.apps import AppConfig


class MotorcyclesConfig(AppConfig):
    name = 'motorcycles'


    def ready(self):
        import motorcycles.signals
        