"""primerProyectoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from clientes_coches.views import ver_clientes, add_clientes
from django.contrib import admin
from django.urls import path

from webapp.views import bienvenido, despedida, listar_alumnos
from deportes.views import deportes, listar_selecciones, add_seleccion, ver_jugadores, add_jugador

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name="inicio"),
    path('goodbye/', despedida),
    path('deportes/', deportes, name="deportes"),
    path('alumnos/listar_alumnos/', listar_alumnos, name="listado_alumnos"),
    path('deportes/futbol/listado-selecciones', listar_selecciones, name="listado_selecciones"),
    path('deportes/futbol/add_seleccion', add_seleccion, name="add_seleccion"),
    path('clientes/ver_clientes', ver_clientes, name="ver_clientes"),
    path('clientes/addCliente', add_clientes, name="add_clientes"),
    path('deportes/jugadores', ver_jugadores, name="ver_jugadores"),
    path('deportes/jugadores/add/', add_jugador, name="add_jugador"),

]
