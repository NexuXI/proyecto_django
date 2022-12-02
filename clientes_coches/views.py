from clientes_coches.models import Cliente
from django.forms import modelform_factory
from django.shortcuts import render


ClienteForm = modelform_factory(Cliente, exclude=[])


# Create your views here.
def add_clientes(request):

    contexto = {}
    return render(request, "add_clientes.html", contexto)


def ver_clientes(request):

    if request.method == 'POST':
        try:
            cliente = Cliente()
            cliente.nombre = request.POST.get("nombre", "")
            cliente.apellidos = request.POST.get("apellidos", "")
            cliente.email = request.POST.get("email", "")
            cliente.dni = request.POST.get("dni", "")
            cliente.save()
            # cliente_form = ClienteForm(request.POST)
            # cliente_form.save()
        except Exception as e:
            print(e)

    # cliente_form = ClienteForm()

    clientes = Cliente.clientes.all()

    contexto = {"clientes": clientes}
    # contexto = {"clientes": clientes, "cliente_form": cliente_form}
    return render(request, "clientes.html", contexto)
