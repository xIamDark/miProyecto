from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
TEMPLATE_DIRS =(
   'os.path.join(BASE_DIR, "templates")' 
)

def index(request):
    context = {}
    return render(request,'venta/index.html',context)
def registro(request):
    context = {}
    return render(request,'venta/registro.html',context)
def login(request):
    context = {}
    return render(request,'venta/login.html',context)
def productos(request):
    context = {}
    return render(request,'venta/productos.html',context)
def nosotros(request):
    context = {}
    return render(request,'venta/nosotros.html',context)
def contacto(request):
    context = {}
    return render(request,'venta/contacto.html',context)
def smarthphone(request):
    context = {}
    return render(request,'venta/smarthphone.html',context)

