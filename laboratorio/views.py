from django.shortcuts import render
from .models import Laboratorio, DirectorGeneral, Producto 

from django.db.models import Q
from django.db.models import Count, Sum, Avg, Min, Max 

from django.shortcuts import render, redirect
from .forms import ProductoFormAdd, LaboratorioFormAdd, LaboratorioFormUpdate
from django.contrib import messages



def listar_laboratorios(request):
    contexto = {}
    laboratorios = Laboratorio.objects.all()
    contexto["laboratorios"] = laboratorios 
    return render(request, "laboratorio/listar_laboratorios.html", contexto)


def add_laboratorio(request):
    contexto = {}
        
    if request.method == 'GET':
        contexto["form"] = LaboratorioFormAdd()
        return render(request, 'laboratorio/add_laboratorio.html', contexto)
    
    if request.method == 'POST':   #
        
        form = LaboratorioFormAdd(request.POST)
        contexto["form"] = form 
        
        print(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Laboratorio creado correctamente.")
            return redirect('listar_laboratorios')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'laboratorio/add_laboratorio.html', contexto)
  
def detalle_laboratorio(request, laboratorio_id):
    contexto = {}

    laboratorio= Laboratorio.objects.order_by('id').get(id=laboratorio_id)
    
    contexto["laboratorio"] = laboratorio
 
   
    return render(request, "laboratorio/detalle_laboratorio.html", contexto)  


def update_laboratorio(request, id_laboratorio):
    
    contexto = {}
    
    ### Fetching the Product:###
    try:  
        laboratorio = Laboratorio.objects.get(id=id_laboratorio) #Producto.objects.get() to retrieve a product from the database by its id.
    	
    	#producto = producto.delete() # para protegerse de cabios de precios.
    # If the product doesn't exist, a DoesNotExist exception is caught, and an error message is shown.    
    except Producto.DoesNotExist: 
        messages.error(request, f"No existe un producto con id: {id_laboratorio}")
        return redirect('listar_laboratorios')
        
    ###  Handling GET Request:####
    if request.method == 'GET': #When the request method is GET, you're preparing the form to update the product:
        
        
    ###Handling POST Request: ####
        #When the request method is POST, you're processing the form data:
        form = LaboratorioFormUpdate(instance=laboratorio) 
        contexto["form"] = form
        
        contexto["laboratorio"] = laboratorio
        return render(request, 'laboratorio/update_laboratorio.html', contexto)
        
        
    if request.method == "POST": #You're also checking if the price and stock values meet certain conditions Price must be greater than 0.Stock must be 0 or more.
        form = LaboratorioFormUpdate(request.POST, instance=laboratorio)
        contexto["form"] = form 
        
        errores = ""
        

        if errores:
            messages.error(request, errores)
            return render(request, 'laboratorio/update_laboratorio.html', contexto)

    
        ##Form Validation:###
        if form.is_valid(): # You check if the form is valid and save the changes:
            form.save()
            messages.success(request, "Laboratorio actualizado con éxito.")
            return redirect('listar_laboratorios')
         
        ## using Django's messaging framework to give feedback to the use   ###
        else:
            messages.error(request, "Revise los datos ingresados en el formulario y vuelva a intentarlo.")
            return render(request, 'laboratorio/update_laboratorio.html', contexto)

 
def delete_laboratorio(request, id_laboratorio):
     
    try:
        laboratorio = Laboratorio.objects.get(id=id_laboratorio)
         
    except Laboratorio.DoesNotExist:
        messages.error(request, f"No existe un laboratorio con id: {id_laboratorio}")
        return redirect('listar_laboratorios')
     
    laboratorio.delete()
         
    messages.success(request, f"Laboratorio con ID: {id_laboratorio} eliminado con éxito.")
    return redirect('listar_laboratorios')











# productos

def listar_productos(request):
       
    # Filtrar por el nombre dado
    nombre = request.GET.get('nombre') # Obtener el nombre desde la URL (si existe)
    precio_min = request.GET.get("precio_min", None)
    precio_max = request.GET.get("precio_max", None)
    fecha_vencimiento_min = request.GET.get("fecha_vencimiento_min", None)
    fecha_vencimiento_max = request.GET.get("fecha_vencimiento_max", None)

    contexto = {}
    productos = Producto.objects.all()
    
    if not nombre:
        nombre = ""
        
    if nombre: # SI ESXISTE
        # Usar __icontains para hacer una búsqueda insensible a mayúsculas y minúsculas
        productos = productos.filter(Q(nombre__icontains=nombre) | Q(despcripcion__icontains= nombre))
               
    if precio_min: #si exsite   
        productos = productos.filter(p_costo__gte=precio_min)#gte mayor que
    if precio_max:
        productos = productos.filter(p_costo__lte=precio_max) #lte - menor que
        
    if fecha_vencimiento_min: #si exsite   
       productos = productos.filter(f_fabricacion__gte=fecha_vencimiento_min)#gte mayor que
    if fecha_vencimiento_max:
        productos = productos.filter(f_fabricacion__lte=fecha_vencimiento_max) #lte - menor que
        
    contexto["productos"] = productos  
    contexto["laboratorios"] = Laboratorio.objects.all()
    contexto["nombre"] = nombre
    contexto["precio_min"] = precio_min
    contexto["precio_max"] = precio_max
    contexto["fecha_vencimiento_min"] = fecha_vencimiento_min
    contexto["fecha_vencimiento_max"] = fecha_vencimiento_max
    
    return render(request, "producto/listar_productos.html", contexto)


def add_producto(request):
    contexto = {}
        
    if request.method == 'GET':
        contexto["form"] = ProductoFormAdd()
        return render(request, 'producto/add_producto.html', contexto)
    
    if request.method == 'POST':   #
        
        form = ProductoFormAdd(request.POST)
        contexto["form"] = form 
        
        print(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Producto creado correctamente.")
            return redirect('listado_productos')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'producto/add_producto.html', contexto)
  
  

def detalle_producto(request, producto_id):
    contexto = {}

    producto= Producto.objects.order_by('id').get(id=producto_id)
    
    contexto["producto"] = producto
 
   
    return render(request, "producto/detalle_producto.html", contexto)