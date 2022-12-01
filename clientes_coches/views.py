from clientes_coches.models import Cliente
from django.shortcuts import render


# Create your views here.
def add_clientes(request):

    contexto = {}
    return render(request, "add_clientes.html", contexto)


def ver_clientes(request):
    if request.method == 'POST':
        cliente = Cliente()
        cliente.nombre = request.POST.get("nombre", "")
        cliente.apellidos = request.POST.get("apellidos", "")
        cliente.email = request.POST.get("email", "")
        cliente.dni = request.POST.get("dni", "")
        cliente.save()

    clientes = Cliente.clientes.all()

    contexto = {"clientes": clientes}
    return render(request, "clientes.html", contexto)
