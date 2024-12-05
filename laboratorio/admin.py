from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

# Register your models here.


@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre'] #filtro 
    ordering = ['nombre']


@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ['nombre',]
    search_fields = ['nombre'] #filtr
    ordering = ['nombre']
    
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre',]
    search_fields = ['nombre'] #filtr
    ordering = ['nombre']

    
