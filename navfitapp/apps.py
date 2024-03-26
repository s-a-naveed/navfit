from django.apps import AppConfig


class NavfitappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'navfitapp'
    
    def ready(self):
        import navfitapp.signals