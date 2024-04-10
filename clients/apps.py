from django.apps import AppConfig

from suit.apps import DjangoSuitConfig


class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'

    
class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'