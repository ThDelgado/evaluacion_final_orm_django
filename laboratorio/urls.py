from django.urls import path
from . import views   

urlpatterns = [
    #laboratorio
    path('laboratorio/', views.listar_laboratorios, name= 'listar_laboratorios'),
    path('laboratorio/add', views.add_laboratorio, name="add_laboratorio"),
    path('laboratorio/detalle/<int:laboratorio_id>', views.detalle_laboratorio, name="detalle_laboratorio"),
    path('laboratorio/update/<int:id_laboratorio>', views.update_laboratorio, name="update_laboratorio"),
    path('laboratorio/delete/<int:id_laboratorio>/', views.delete_laboratorio, name="delete_laboratorio"),
  
   #productos
    path('productos/', views.listar_productos, name= 'listar_productos'),
    path('productos/add', views.add_producto, name="add_producto"),
    path('productos/detalle/<int:producto_id>', views.detalle_producto, name="detalle_producto"),

]
