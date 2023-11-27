from django.apps import AppConfig


class CategoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.category"


#    """
#     Configuración de la aplicación 'category'.
#     """

# default_auto_field = "django.db.models.BigAutoField"
# Especifica el campo de clave primaria automático a utilizar para los modelos.
# En este caso, se utiliza un campo grande (`BigAutoField`).

# name = "apps.category"
# Nombre de la aplicación. En este caso, la aplicación se llama 'category'.
