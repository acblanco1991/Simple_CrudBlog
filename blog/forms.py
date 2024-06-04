from django import forms
from blog.models import Blog, Categoria
from . import models
from ckeditor.widgets import CKEditorWidget
from .models import Blog

# class BlogAgregarForm(forms.Form):
#     titulo= forms.CharField(help_text="Entre un titulo")
#
#     # class Meta:
#     #     model = models.Blog
#     #     fields = '__all__'
#     #     widgets = {
#     #         'titulo': forms.TextInput(attrs={'class': 'form-control'}),
#     #         'contenido': forms.TextInput(),
#     #         'categoria': forms.ChoiceField(),
#     #     }

class CatForm(forms.ModelForm):
    # titulo= forms.CharField(help_text="Entre un titulo")
    # contenido=forms.

    class Meta:
        model = models.Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'id': 'name', 'class': 'form-control'})
        }

# class BlogEditForm(forms.ModelForm):
class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            # 'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'contenido': forms.CharField(widget=CKEditorWidget()),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class Filtro(forms.Form):
    opcion = forms.CharField(label='Opción',
                             widget=forms.Select(choices=[('opcion1', 'Opción 1'), ('opcion2', 'Opción 2')]))


# class BlogFilterForm(forms.Form):
#     categoria = forms.ChoiceField(
#         choices=[(blog.categoria, blog.categoria) for blog in
#                  Blog.objects.values_list('categoria', flat=True).distinct()],
#         required=False,
#         widget=forms.Select
#     )


# class BlogFilterForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         categorias = kwargs.pop('categorias', [])
#         super(BlogFilterForm, self).__init__(*args, **kwargs)
#         self.fields['categoria'] = forms.ChoiceField(
#             choices=[('', 'Selecciona una categoría')] + [(categoria, categoria) for categoria in categorias],
#             required=False,
#             widget=forms.Select
#         )
# class MyModelForm(forms.ModelForm):
#     contenido = forms.CharField(widget=CKEditorWidget())
#
#     class Meta:
#         model = Blog
#         fields = ('contenido',)