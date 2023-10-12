from django.apps import AppConfig

class ProductoConfig(AppConfig):
    name = 'producto'

    def ready(self):
        import producto.signal
