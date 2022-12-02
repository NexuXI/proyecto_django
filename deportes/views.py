from deportes.models import Jugador
from django.shortcuts import render


# Create your views here.
def deportes(request):
    contenido = {"titulo_pagina": "Actualidad deportiva",
                 "descripcion": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod "
                                "tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, "
                                "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "}
    return render(request, "deportes.html", contenido)


def add_seleccion(request):
    listado_continentes = ["Europa", "America", "Asia", "Africa", "Oceania"]
    titulo = None
    if request.method == 'POST':
        continente_filtro = request.POST['continente']
        titulo = request.POST['titulo']

    contexto = {"titulo": titulo, "listado_continentes": listado_continentes}
    return render(request, "add_seleccion.html", contexto)


def listar_selecciones(request):
    continente_filtro = None
    nombre_nueva_seleccion = None
    continente_nueva_seleccion = None
    num_mundiales_nueva_seleccion = None
    if request.method == 'POST':
        continente_filtro = request.POST.get("continente", "")
        nombre_nueva_seleccion = request.POST.get("nombre", "")
        continente_nueva_seleccion = request.POST.get("continente_seleccion", "")
        num_mundiales_nueva_seleccion = request.POST.get("num_mundiales", "")
        titulo = request.POST.get("titulo", "")

    elif request.method == 'GET':
        # titulo = request.parameter("titulo")
        titulo = request.GET.get('titulo', "")

    espania = {"nombre": "España", "continente": "Europa", "num_mundiales": 1}
    brasil = {"nombre": "Brasil", "continente": "America", "num_mundiales": 5}
    francia = {"nombre": "Francia", "continente": "Europa", "num_mundiales": 2}
    senegal = {"nombre": "Senegal", "continente": "Africa", "num_mundiales": 0}

    lista_selecciones = [espania, brasil, francia, senegal]

    nuevo_pais = {"nombre": nombre_nueva_seleccion, "continente": continente_nueva_seleccion, "num_mundiales": num_mundiales_nueva_seleccion}

    if nombre_nueva_seleccion is not None and continente_nueva_seleccion is not None and num_mundiales_nueva_seleccion is not None:
        lista_selecciones.append(nuevo_pais)

    if continente_filtro is not None and continente_filtro == "":
        lista_selecciones = list(
            filter(lambda seleccion: seleccion["continente"] == continente_filtro, lista_selecciones))

    contexto = {"listado_selecciones": lista_selecciones, "titulo_tabla": titulo,
                "listado_continentes": ["Europa", "America", "Asia", "Africa", "Oceania"]}

    return render(request, "listado_selecciones_mundial.html", contexto)


def ver_jugadores(request):
    if request.method == 'POST':
        # Filtros
        posicion_filtro = request.POST.get("posicion", "")
        nacionalidad_filtro = request.POST.get("nacionalidad", "")
        equipo_filtro = request.POST.get("equipo", "")
        # Nuevo jugador
        jugador = Jugador()
        jugador.nombre = request.POST.get("nombre_jugador", "")
        jugador.equipo = request.POST.get("equipo_jugador", "")
        jugador.edad = request.POST.get("edad_jugador", "")
        jugador.nacionalidad = request.POST.get("nacionalidad_jugador", "")
        jugador.posicion = request.POST.get("posicion_jugador", "")
        jugador.save()

    posiciones = ['Delantero', 'Centrocampista', 'Defensa', 'Portero']
    nacionalidades = Jugador.jugadores.values_list("nacionalidad", flat=True)
    equipos = Jugador.jugadores.values_list("equipo", flat=True)
    jugadores = Jugador.jugadores.all().order_by('nombre')

    contexto = {"posiciones": posiciones, "nacionalidades": nacionalidades, "equipos": equipos, "jugadores": jugadores}
    return render(request, "jugadores.html", contexto)


def add_jugador(request):
    posiciones = ['Delantero', 'Centrocampista', 'Defensa', 'Portero']
    contexto = {"posiciones": posiciones}
    return render(request, "add_jugador.html", contexto)
