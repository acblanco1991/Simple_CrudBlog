from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView, ListView
from django.views.generic import edit
from django.http import HttpResponseRedirect
from blog.models import *
from blog.forms import *
from django.urls import reverse
from .models import Categoria, Blog
from django.contrib import messages
from django.views import generic, View
from django.shortcuts import render, redirect


# # Create your views here.
def BlogList(request):
    blog = Blog.objects.all()
    return render(request, "index.html", {"blog": blog})


def BlogCreate(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        contenido = request.POST.get('contenido', '')
        nuevo_blog = Blog(titulo=titulo, contenido=contenido)
        nuevo_blog.save()
        messages.success(request, '¡Guardado Correctamente!')
        return redirect('/')


def BlogDetail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, "details.html", {"blog": blog})


def BlogEdit(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.titulo = request.POST.get('titulo')
        blog.contenido = request.POST.get('contenido')
        # blog.categoria = request.POST.get('categoria')as
        blog.save()
        messages.success(request, '->' + blog.titulo + ' ¡Editado Correctamente!')
        return redirect('/')
    return render(request, "edit.html", {"blog": blog})


def BlogDelete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request, '¡Eliminado Correctamente!')
    return redirect('/')


def buscar_productos(request):
    query = request.GET.get('datos', '')  # Obtener el término de búsqueda de la consulta GET
    print(query)
    blog = Blog.objects.filter(titulo__icontains=query)  # Filtrar productos por nombre
    print(blog)
    return render(request, 'index.html', {'blog': blog})


class CategoriaList(ListView):
    model = models.Categoria
    template_name = 'categoria.html'

    # success_url = reverse_lazy('categoria.html')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        form = CatForm()
        context["form"] = form
        print(context)

        return context
    # def get_queryset(self):
    #
    # def get(self, request):
    #     categoria = Categoria.objects.all()
    #     self.model.objects.all()
    #     return render(request, 'categoria.html', {'categoria': categoria})


class CategoriaCreate(CreateView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    template_name = 'categoria.html'
    form_class = CatForm
    # fields = ['nombre', 'descripcion']

    # def form_valid(self, form):
    #
    # def form_invalid(self, form):


class CategoriaDetail(DetailView):
    model = models.Categoria
    template_name = 'detail_categ.html'


class CategoriaEdit(edit.UpdateView):
    model = models.Categoria
    template_name = 'edit_categ.html'
    success_url = reverse_lazy('categoria_list')
    fields = ['nombre', 'descripcion']


class CategoriaDelete(edit.DeleteView):
    model = models.Categoria
    template_name = 'delete_categ.html'
    success_url = reverse_lazy('categoria_list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["aymarin"] = 'aymaas'
        print(context)

        return context

    # def delete(self, request, *args, **kwargs):
    #     """
    #     Elimina la categoría y muestra el mensaje de éxito después de la eliminación.
    #     """
    #     result = super().delete(request, *args, **kwargs)
    #     messages.success(request, '¡Eliminado Correctamente!')
    #     return result

    # def dispatch(self, request):
    #     messages.success(request, '¡Eliminado Correctamente!')
    #     return super().delete(request)
