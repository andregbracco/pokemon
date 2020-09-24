from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Region, Tipo, Pokemon

class ListAllPokemon(ListView):
	template_name = 'bichos/listapokemon.html'
	paginate_by = 10
	ordering = "-id"
	model = Pokemon


class ListaRegion(ListView):
	template_name = 'bichos/lista_region.html'

	def get_queryset(self):
		zona = self.kwargs['zona']
		lista = Pokemon.objects.filter(region__name = zona)
		return lista


class ListaRegionByKword(ListView):
	template_name = 'bichos/by_kword.html'
	context_object_name = 'bichos'

	def get_queryset(self):
		nombre_region_buscada = self.request.GET.get("nombre_cargado_usuario",)
		return Pokemon.objects.filter(region__name = nombre_region_buscada)


class DatosPokemon(DetailView):
	model = Pokemon
	template_name = 'bichos/detalle-pokemon.html'

	def get_context_data(self, **kwargs):
		context = super(DatosPokemon, self).get_context_data(**kwargs)
		return context

class SuccessView(TemplateView):
	template_name = "bichos/success.html"

class CrearPokemon(CreateView):
	model = Pokemon
	template_name = 'bichos/agregar.html'
	fields = [
		'name',
		'pc',
		'ps',
		'region',
		'tipos'
	]
	success_url = reverse_lazy('bicho_app:correcto')

class ModificarBicho(UpdateView):
	model = Pokemon
	template_name = 'bichos/modificar.html'
	fields = [
		'name',
		'pc',
		'ps',
		'region',
		'tipos'
	]
	success_url = reverse_lazy('bicho_app:correcto')


	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):

		return super(ModificarBicho, self).form_valid(form)

class BorrarPokemon(DeleteView):
	template_name = 'bichos/borrar.html'
	model = Pokemon
	context_object_name = 'pokemon'
	success_url = reverse_lazy('bicho_app:correcto')

















