from django.contrib import admin
from .models import Categoria, Blog
# from fun.models import Playground

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categoria)

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Blog)


