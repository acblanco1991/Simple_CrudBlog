from django import forms
from blog.models import Blog
from . import models

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }

class CatForm(forms.ModelForm):

    class Meta:
        model = models.Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'id': 'name'})
        }


