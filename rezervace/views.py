from django.shortcuts import render
from .models import Rezervace, Zakaznik
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

def index(request):
    context = {
        'nadpis': 'Rezervační web',
        'rezervace': Rezervace.objects.all(),
        'zakaznici' : Zakaznik.objects.order_by('prijmeniZakaznika')
    }
    return render(request, 'index.html', context=context)

def zakaznici(request):
    context = {
        'zakaznici': Zakaznik.objects.all(),
    }
    return render(request, 'zakaznici.html', context=context)