from django.apps import AppConfig

class TonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Projet_annee'
	
    def ready(self):
        import Projet_annee.signals