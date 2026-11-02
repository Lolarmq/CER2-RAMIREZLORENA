from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/<int:id>/', views.detalle, name='detalle'),
    path('categorias/',views.categorias,name = 'categorias'),
    path('categorias/<int:id>/',views.filtrar_categoria, name = 'filtrar_categoria'),
    path('gestion/',views.gestion,name = 'gestion'),
    path('gestion/agregar/',views.agregar_lugar,name = 'agregar_lugar'),
    path('gestion/editar/<int:id>/',views.editar_lugar,name = 'editar_lugar'),
]