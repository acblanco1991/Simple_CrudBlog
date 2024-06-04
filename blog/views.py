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
from django.http import JsonResponse
from django.core import serializers


# # Create your views here.
def BlogList(request):
    blog = Blog.objects.all()
    opcion= Categoria.objects.all()
    return render(request, "index.html", {"blog": blog, "opcion": opcion})

def BlogCreate(request):
    form = BlogForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            blog = form.save(commit=False)
            if 'imagen' not in request.FILES:
                default_image = '/fotos/IMG-20231106-WA0184.jpg'  # Ruta a la imagen por defecto
                blog.imagen = default_image
            blog.save()
            form.save()
            return HttpResponseRedirect(reverse('blog_list'))

    return render(request, 'create.html', {'form': form})

def BlogDetail(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)
    for field in form.fields.values():
        field.widget.attrs['readonly'] = True
    return render(request, "details.html", {"blog": blog, "form": form})

def BlogEdit(request, id):
    blog = get_object_or_404(Blog,id=id)
    form = BlogForm(request.POST or None, instance=blog)  # Initialize with existing data
    if request.method == 'POST':

        if form.is_valid():

            blog.titulo = form.cleaned_data['titulo']
            blog.contenido = form.cleaned_data['contenido']
            blog.categoria = form.cleaned_data['categoria']
            blog.imagen = form.cleaned_data['imagen']
            # if blog.imagen:
            #     blog.imagen = generate_unique_filename(blog.imagen)

            blog.save()  # Update the blog object
            messages.success(request, '->' + blog.titulo + ' ¡Editado Correctamente!')
            return redirect('/')
    return render(request, "edit.html", {"blog": blog, "form": form})


def BlogDelete(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('/')
    return render(request, "delete.html", {"blog": blog})


def buscar_blog(request):

        query = request.GET.get('datos', '')
        blog = Blog.objects.filter(titulo__icontains=query)
        if not blog.exists():
            messages.success(request, '¡No hay blog con ese título!')
            return redirect('/')
        return render(request, 'index.html', {'blog': blog})

def buscar_categ(request):
    query = request.GET.get('datos', '')
    categ = Categoria.objects.filter(nombre__icontains=query)
    return render(request, 'categoria.html', {'categ': categ})


def filtrar_categ(request):
    if request.method == 'POST':
        opcion = request.POST.get('datos1')
        try:
            categoria = Categoria.objects.get(nombre=opcion)
            blog = Blog.objects.filter(categoria=categoria)
            if not blog.exists():
                return JsonResponse({'error': 'No hay blogs en esta categoría'}, safe=False)
        except Categoria.DoesNotExist:
            blog = Blog.objects.all()
            return JsonResponse({'blog': blog}, safe=False)

        blog_list = []
        for b in blog:
            blog_list.append({
                'titulo': b.titulo,
                'contenido': b.contenido,
                'categoria': b.categoria.nombre,
                'imagen': b.imagen.url,
                'id': b.id
            })
        return JsonResponse({'blog': blog_list}, safe=False)
    else:
        blog = Blog.objects.all()
    return render(request, 'index.html', {"blog": blog})

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
        return context

class CategoriaCreate(CreateView):
    model = Categoria
    success_url = reverse_lazy('categoria_list')
    template_name = 'create_categ.html'
    form_class = CatForm

class CategoriaDetail(DetailView):
    model = models.Categoria
    template_name = 'detail_categ.html'
    # form_class = CatForm

# Analizar esto
#     def get_context_data(self, *kwargs):
#         context = super(self).get_context_data(*kwargs)
#         context['categoria'] = self.object
#         return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class CategoriaEdit(edit.UpdateView):
    model = models.Categoria
    template_name = 'edit_categ.html'
    form_class = CatForm
    success_url = reverse_lazy('categoria_list')
    # fields = ['nombre', 'descripcion']


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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})
