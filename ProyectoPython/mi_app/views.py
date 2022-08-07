from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    return HttpResponse("Hola Django - Coder")

def indice(request):
    variable = {"variable": "hola"}
    return render(request, "mi_app/index.html", variable)

