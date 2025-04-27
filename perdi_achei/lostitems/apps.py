# lostitems/apps.py

from django.apps import AppConfig

class LostitemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lostitems'
    verbose_name = 'Itens Perdidos'