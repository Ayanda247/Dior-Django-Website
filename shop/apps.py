# shop/apps.py

from django.apps import AppConfig

class ShopConfig(AppConfig):
    """
    Configuration for the 'shop' application.

    :param default_auto_field: The default auto field type for models in this app.
    :type default_auto_field: str
    :param name: The name of the application.
    :type name: str

    :return: None
    :rtype: None
    """
    
    # The default primary key field type to use for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # The name of the application
    name = 'shop'


