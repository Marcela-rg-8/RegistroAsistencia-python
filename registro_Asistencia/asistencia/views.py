from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Inicio")
   
def areaPersonal(request):
    return HttpResponse("AreaPersonal")

def profile(request):
    return HttpResponse("Perfil")  

  