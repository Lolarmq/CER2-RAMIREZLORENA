from django.shortcuts import render,get_object_or_404
from .models import LugarPatrimonial,Categoria
from django.shortcuts import redirect
from .forms import LugarPatrimonialForm
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def inicio(request):
    return render(request,'patrimonio/inicio.html')

def catalogo(request):
    lugares = LugarPatrimonial.objects.all()
    return render(request,'patrimonio/catalogo.html',{'lugares':lugares})

def detalle(request,id):
    lugar = get_object_or_404(LugarPatrimonial, id = id)
    return render(request,'patrimonio/detalle.html',{'lugar':lugar})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request,'patrimonio/categorias.html',{'categorias': categorias})

def filtrar_categoria(request,id):
    categoria = get_object_or_404(Categoria, id = id)
    lugares = LugarPatrimonial.objects.filter(categoria = categoria)
    return render(request,'patrimonio/catalogo.html',{'lugares':lugares})

@login_required
def gestion(request):
    lugares = LugarPatrimonial.objects.all()
    return render(request,'patrimonio/gestion.html',{'lugares':lugares})

@login_required
@permission_required('patrimonio.add_lugarpatrimonial',raise_exception = True)
def agregar_lugar(request):
    if request.method == 'POST':
        formulario = LugarPatrimonialForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('gestion')
    else:
        formulario = LugarPatrimonialForm()
    return render(request,'patrimonio/formulario_lugar.html',{'formulario':formulario})

@login_required
@permission_required('patrimonio.change_lugarpatrimonial',raise_exception = True)
def editar_lugar(request,id):
    lugar = get_object_or_404(LugarPatrimonial,id = id)
    if request.method == 'POST':
        formulario = LugarPatrimonialForm(request.POST,instance = lugar)
        if formulario.is_valid():
            formulario.save()
            return redirect('gestion')
    else:
        formulario = LugarPatrimonialForm(instance = lugar)
    return render(request,'patrimonio/formulario_lugar.html',{'formulario':formulario})
    
