from django.forms import ModelForm    
from django import forms   
 
from .models import Producto, Laboratorio 

class LaboratorioFormAdd(ModelForm):    # cLASES EN UPPERCAMELCASE
    class Meta:
        model = Laboratorio 
        fields = [

            'nombre', 
            'pais', 
            'ciudad', 
            ]

        
        help_texts = {

        }
        
        widgets = {
            "nombre": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "pais": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "ciudad": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "imagen": forms.URLInput(attrs={"class": 'form-control', 'placeholder': 'Ingrese la URL de la imagen'}),
        }
    
class ProductoFormAdd(ModelForm):    # cLASES EN UPPERCAMELCASE
    class Meta:
        model = Producto
        fields = [
            'nombre', 
            'descripcion', 
            'p_costo', 
            'p_venta', 
            'f_fabricacion', 
            'laboratorio'
            ]

        labels = {
            "descripcion": ("Descripción"),
            "laboratorio": ("Laboratorio"),
            "p_costo": ("Precio de costo"),
            "p_venta": ("Precio de venta"),
            "f_fabricacion": ("Fecha de creacion")
            
        }
        
        help_texts = {
            "nombre": ("* El nombre debe contener sólo letras, espacio, -"),
            "precio": ("* El precio debe ser mayor a 0"),
        }
        
        widgets = {
            "nombre": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "descripcion": forms.Textarea(attrs={"class": 'form-control', "rows": 3}),
            "p_costo": forms.NumberInput(attrs={"class": 'form-control', 'min': 1}),
            "p_venta": forms.NumberInput(attrs={"class": 'form-control', 'min': 1}),
            "f_fabricacion": forms.DateInput(attrs={"class": 'form-control', 'type': 'date'}),
            "laboratorio": forms.Select(attrs={"class": 'form-control'}),
        }
    


class LaboratorioFormUpdate(ModelForm):
    class Meta:
        model = Laboratorio 
        fields = [
            'nombre', 
            'ciudad', 
            'pais', 
            'imagen', 
            ]

         
        widgets = {
            "nombre": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "ciudad": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "pais": forms.TextInput(attrs={"class": 'form-control', 'maxlength': 50}),
            "imagen": forms.URLInput(attrs={"class": 'form-control', 'placeholder': 'Ingrese la URL de la imagen'}),
        }       
 
 