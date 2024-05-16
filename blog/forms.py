from django import forms
from blog.models import Blog
from . import models

class BlogAgregarForm(forms.Form):
    titulo= forms.CharField(help_text="Entre un titulo")

    # class Meta:
    #     model = models.Blog
    #     fields = '__all__'
    #     widgets = {
    #         'titulo': forms.TextInput(attrs={'class': 'form-control'}),
    #         'contenido': forms.TextInput(),
    #         'categoria': forms.ChoiceField(),
    #     }

class CatForm(forms.ModelForm):
    # titulo= forms.CharField(help_text="Entre un titulo")
    # contenido=forms.

    class Meta:
        model = models.Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'id': 'name'})
        }

# class BlogEditForm(forms.ModelForm):
