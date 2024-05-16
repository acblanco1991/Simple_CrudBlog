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
    cate=Categoria.objects.all()
    form = BlogForm
    conntext ={"blog": blog, "cate": cate,'form':form }
    return render(request, "index.html",conntext )

def BlogCreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog_list'))

def BlogDetail(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, "details.html", {"blog": blog})

def BlogEdit(request, pk):
    blog = Blog.objects.get(id=pk)
    print(request.method)
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog.titulo=form.cleaned_data['titulo']
            blog.contenido=form.cleaned_data['contenido']
            blog.categoria=form.cleaned_data['categoria']
            blog.save()
            return redirect(reverse('blog_detail',args=[pk]))
    else:
        form = BlogForm(instance=blog)
        return render(request, "edit.html", {"form": form})

# def BlogEdit(request, pk):
#     blog = Blog.objects.get(id=pk)
#     if request.method == 'POST':
#         blog.titulo = request.POST.get('titulo')
#         blog.contenido = request.POST.get('contenido')
#         # blog.categoria = request.POST.get('categoria')
#         blog.save()
#         messages.success(request, '->' + blog.titulo + ' ¡Editado Correctamente!')
#         return redirect('/')
#     return render(request, "edit.html", {"blog": blog})


def BlogDelete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request, '¡Eliminado Correctamente!')
    return redirect('/')


def buscar_productos(request):
    query = request.GET.get('datos', '')  # Obtener el término de búsqueda de la consulta GET
    blog = Blog.objects.filter(titulo__icontains=query)  # Filtrar productos por nombre
    return render(request, 'index.html', {'blog': blog})


class CategoriaList(ListView):
    model = models.Categoria
    template_name = 'categoria.html'



    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        form = CatForm()
        context["form"] = form

        return context


class CategoriaCreate(CreateView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    template_name = 'categoria.html'
    form_class = CatForm



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
