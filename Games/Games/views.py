from tkinter import Entry
from django.shortcuts import render
from Games.models import PgPrincipal
from django.http import HttpResponse

# Create your views here.
def index(request):
    all_products = PgPrincipal.objects.all() 
    return render(request, "index.html", {"guitarras": all_products})

def test1(request):
    #all_entries = Site.objects.get(id=1)
    #resulta = []
    #for x in all_entries:
    #    formatador = "x.nome.card+"
    #    resulta.append()
    retornar = all_entries.nome_card + " | " + all_entries.description + " | "

    return HttpResponse(retornar)