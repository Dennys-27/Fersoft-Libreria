
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')


#funcion de para ver un vist html
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

#funcion de para ver un vist html index de blog libros
def libros(request):
    libros = Libro.objects.all()  # no necesitas el punto y coma
    context = {
        'libros': libros
    }
    return render(request, 'libros/index.html', context)


#crear libros
def create(request):
    formulario = LibroForm(request.POST or None, request.FILES or None)
    
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/create.html', {'formulario' : formulario})


#crear libros
def edit(request,id):
    libro = Libro.objects.get(id = id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/edit.html', {'formulario' : formulario})

def delete(request, id):
    libro = Libro.objects.get(id = id)
    libro.delete()
    return redirect('libros')
