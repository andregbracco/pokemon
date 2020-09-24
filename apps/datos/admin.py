from django.contrib import admin
from .models import *

# Register your models here.

class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'region',
        'pc',
        'ps',
    )
    
    search_fields = ('name',)
    list_filter = ('region', 'tipos')
    filter_horizontal = ('tipos',)

admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Region)
admin.site.register(Tipo)
