from django.db import models


# Create your models here.
class Category(models.Model):
    """
    Modelo para representar categorías en la base de datos.
    """

    class Meta:
        verbose_name = (
            "Category"  # Nombre descriptivo singular para la interfaz de administración
        )
        verbose_name_plural = (
            "Categories"  # Nombre descriptivo plural para la interfaz de administración
        )

    parent = models.ForeignKey(
        "self",  # Clave externa que establece una relación consigo misma
        related_name="children",  # Permite acceder a las categorías secundarias desde una categoría principal
        on_delete=models.CASCADE,  # Si el padre se elimina, las categorías secundarias también se eliminan
        blank=True,  # El campo puede ser opcional en formularios
        null=True,  # El campo puede ser nulo en la base de datos
    )

    name = models.CharField(max_length=255, unique=True)
    # Campo para almacenar el nombre de la categoría con una longitud máxima de 255 caracteres y asegurando unicidad.

    thumbnail = models.ImageField(upload_to="media/categories/")
    # Campo para almacenar una imagen asociada a la categoría en la carpeta "media/categories/".

    def __str__(self):
        """
        Método para representar la instancia como una cadena.
        Devuelve el nombre de la categoría.
        """
        return self.name

    def get_thumbnail(self):
        """
        Método para obtener la URL de la miniatura de la categoría.
        Retorna la URL de la miniatura si está presente, o una cadena vacía si no hay miniatura.
        """
        if self.thumbnail:
            return self.thumbnail.url
        return ""
