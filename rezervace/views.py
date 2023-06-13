from django.shortcuts import render
from .models import Rezervace, Zakaznik

def index(request):
    context = {
        'nadpis': 'Rezervační web',
        'rezervace': Rezervace.objects.all(),
        'zakaznici' : Zakaznik.objects.order_by('prijmeniZakaznika')
    }
    return render(request, 'index.html', context=context)