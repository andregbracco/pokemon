from django.urls import path
from . import views

app_name = 'bicho_app'

urlpatterns = [
    path('listar-todo-bichos', views.ListAllPokemon.as_view(), name='bichosall'),
    path('listar-region/<zona>', views.ListaRegion.as_view()),
    path('listar-por-region/', views.ListaRegionByKword.as_view()),
    path('datos-bicho/<pk>', views.DatosPokemon.as_view(), name='detallebicho'),
    path('success', views.SuccessView.as_view(), name='correcto'),
    path('agregar-pokemon', views.CrearPokemon.as_view()),
    path('modificar-pokemon/<pk>', views.ModificarBicho.as_view(), name='modificar_bicho'),
    path('borrar-pokemon/<pk>', views.BorrarPokemon.as_view(), name='eliminar_bicho')


]