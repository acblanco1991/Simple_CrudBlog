from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.BlogList, name='blog_list'),
    path('create/', views.BlogCreate, name='blog_create'),
    path('lista/', views.BlogList, name='blog_list'),
    path('detail/<int:pk>', views.BlogDetail, name='blog_detail'),
    path('edit/<int:pk>', views.BlogEdit, name='blog_edit'),
    path('delete/<int:id>', views.BlogDelete, name='blog_delete'),
    path('buscador/', views.buscar_productos, name='buscar_productos'),

    path('createcateg/', views.CategoriaCreate.as_view(), name='categoria_create'),
    path('list_categ/', views.CategoriaList.as_view(), name='categoria_list'),
    path('delete_categ/<int:pk>', views.CategoriaDelete.as_view(), name='categoria_delete'),
    path('detail_categ/<int:pk>', views.CategoriaDetail.as_view(), name='categoria_detail'),
    path('edit_categ/<int:pk>', views.CategoriaEdit.as_view(), name='categoria_edit'),
    # path('register/', views.register, name='register'),


]
