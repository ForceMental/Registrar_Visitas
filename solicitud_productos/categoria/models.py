from django.db import models

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        db_table = 'categoria'
