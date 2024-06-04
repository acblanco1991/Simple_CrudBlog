from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
import blog

class Categoria(models.Model):
    nombre = models.CharField(max_length=20, null=True)
    descripcion = models.CharField(max_length=100, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre

class Blog(models.Model):
    titulo = models.CharField(max_length=50, null=True)
    contenido = RichTextField()
    # contenido = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='fotos/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blog'

    def __str__(self):
        return self.titulo


