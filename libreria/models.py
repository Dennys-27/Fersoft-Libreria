from django.db import models

class Libro(models.Model):
    # No es necesario declarar 'id' si solo quieres el auto‐incremental por defecto.
    # Django lo crea automáticamente.
    
    titulo = models.CharField(
        max_length=100,
        verbose_name="Título"
    )
    imagen = models.ImageField(
        upload_to='imagenes/',
        verbose_name="Imagen de portada",
        null=True,
        blank=True
    )
    descripcion = models.TextField(
        verbose_name="Descripción",
        null=True,
        blank=True
    )

    def __str__(self):
        fila = "Titulo: " +self.titulo + " - " + "Descripción: "  + self.descripcion
        return fila
    
    def delete(self, using = None, Keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        