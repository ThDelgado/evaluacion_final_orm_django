SIMULADOR PARA FABRICA DE PRODUCTOS FARMACEUTICOS 


Practica de consolidacion

Para clonar:
https://github.com/ThDelgado/evaluacion_final_orm_django.git


Thelma Delgado




PASSWORD DE TODOS LOS USUARIOS DEL PROYECTO
-------------------------------------






superuser
------
nombre: admin
email: admin@admin.cl
clave: admin


		
pasos para instalar DEPENDENCIAS
------------------------------------------

    1-instalar entorno virtual:
        py.exe -m venv venv
    2- activar entorno virtual
        .\venv\scripts\activate
    3- restaurar DEPENDENCIAS
        pip install -r .\requirements.txt



EDITAR DATOS PARA BD EN SETTINGS.PY
----------------------------------
Debe editar las credenciales de acceso a la base de datos

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "db_final_orm",
        "USER": "userdjango",
        "PASSWORD": "userdjango",
        "HOST": "127.0.0.1",
        "PORT": "5432",
       
    }
}

COMPROBACION DE BASE DE DATOS-
------------------------------------
(venv) PS C:\workspace_m7\practica_final_orm_django> python manage.py dbshell 
psql (14.3)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

db_final_orm=> select now();
              now
-------------------------------
 2024-12-03 20:26:22.985972-03
(1 row)




Por medio de la consola interpretador de python (shell), realice las siguientes consultas: ○ Obtenga todos los objetos 
tanto Laboratorio, DirectorGeneral y Productos.  


Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from laboratorio.models import Laboratorio,DirectorGeneral, Producto 
>>> laboratorio = Laboratorio.objects.all()
>>> directorGeneral = DirectorGeneral.objects.all()
>>> producto = Producto.objects.all()
>>> print(laboratorio)
<QuerySet [<Laboratorio: Gsk>, <Laboratorio: Merck>, <Laboratorio: MSD>]>
>>> print(directorGeneral)
<QuerySet [<DirectorGeneral: Pedro  Maritinez>, <DirectorGeneral: Laura Smith>, <DirectorGeneral: Ronald Mesh>]>
>>> print(producto)
<QuerySet [<Producto: Vacuna  Papiloma>, <Producto: Vacuna papiloma>, <Producto: Vacuna hexavalente>, <Producto: vacuna gardasil tetravalente>]>
>>>




○ Obtenga el laboratorio del Producto cuyo nombre es ‘Producto 1’.

>>> from laboratorio.models import Laboratorio, Producto, Direct
orGeneral
>>> laboratorio = Laboratorio.objects.all().filter(producto__nom
bre='producto 1')
>>> print(laboratorio)
<QuerySet []>



○ Ordene todos los productos por nombre, 
  y que muestre los valores de nombre y laboratorio. 



>>> from laboratorio.models import Laboratorio, Producto, DirectorGeneral
>>> productos = Producto.objects.all().order_by('nombre')  
>>> for producto in productos
  File "<console>", line 1
    for producto in productos
                             ^
SyntaxError: expected ':'
>>> for producto in productos:
...     print("Producto:", producto.nombre)
...     print("Laboratorio: ", producto.laboratorio.nombre)
...
Producto: producto  1
Laboratorio:  Gsk
Producto: Vacuna  Papiloma
Laboratorio:  Gsk
Producto: vacuna gardasil tetravalente
Laboratorio:  Gsk
Producto: Vacuna hexavalente
Laboratorio:  Merck
Producto: Vacuna papiloma
Laboratorio:  MSD
>>> 




○ Realice una consulta que imprima por pantalla los laboratorios 
  de todos los productos.  

>>> from laboratorio.models import Producto
>>> for producto in productos:
...     print("Producto:", producto.nombre)
...     print("Laboratorio:", producto.laboratorio.nombre)
...
Producto: producto  1
Laboratorio: Gsk
Producto: Vacuna  Papiloma
Laboratorio: Gsk
Producto: vacuna gardasil tetravalente
Laboratorio: Gsk
Producto: Vacuna hexavalente
Laboratorio: Merck
Producto: Vacuna papiloma
Laboratorio: MSD
>>>