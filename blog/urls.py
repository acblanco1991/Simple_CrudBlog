from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.BlogList, name='blog_list'),
    path('create/', views.BlogCreate, name='blog_create'),
    path('lista/', views.BlogList, name='blog_list'),
    path('detail/<int:id>', views.BlogDetail, name='blog_detail'),
    path('edit/<int:id>', views.BlogEdit, name='blog_edit'),
    path('delete/<int:id>', views.BlogDelete, name='blog_delete'),
    path('buscar_blog/', views.buscar_blog, name='buscar_blog'),
    path('filtrar_categ/', views.filtrar_categ, name='filtrar_categ'),

    path('createcateg/', views.CategoriaCreate.as_view(), name='categoria_create'),
    path('list_categ/', views.CategoriaList.as_view(), name='categoria_list'),
    path('delete_categ/<int:pk>', views.CategoriaDelete.as_view(), name='categoria_delete'),
    path('detail_categ/<int:pk>', views.CategoriaDetail.as_view(), name='categoria_detail'),
    path('edit_categ/<int:pk>', views.CategoriaEdit.as_view(), name='categoria_edit'),
    path('buscar_categ/', views.buscar_categ, name='buscar_categ'),
    path('accounts/register/', views.register, name='register'),
]
