from django.shortcuts import render, HttpResponse, redirect
from .models import Provisiones
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'GET':

        provisiones = Provisiones.objects.all().order_by('-fecha')
        return render(request, "lista_provisiones.html", {
            "viewname": "Lista de Provisiones",
            "provisiones": provisiones
        })
    elif request.method == 'POST':
        print(request.POST)
        if 'provision' in request.POST and request.POST['provision'] != "":
            provision = Provisiones()
            provision.provision = request.POST['provision']
            messages.add_message(request, messages.SUCCESS,
                                 'Provisión creada con éxito')
            provision.save()
        elif 'provision' in request.POST and request.POST['provision'] == "":
            messages.add_message(request, messages.WARNING,
                                 'La provisión no puede ser vacia')
        elif 'comprando[]' in request.POST and len(request.POST['comprando[]']) > 0:
            print(request.POST.getlist('comprando[]'))
            for ids in request.POST.getlist('comprando[]'):
                obj = Provisiones.objects.get(pk=ids)
                obj.comprado = True
                obj.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Provisiones Actualizadas!')

        return redirect('homeprovisiones')
