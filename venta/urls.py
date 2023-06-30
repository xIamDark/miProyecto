from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('registro',views.registro,name='registro'),
    path('login',views.login,name='login'),
    path('productos',views.productos,name='productos'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('contacto',views.contacto,name='contacto'),
    path('smarthphone',views.smarthphone,name='smarthphone'),















]