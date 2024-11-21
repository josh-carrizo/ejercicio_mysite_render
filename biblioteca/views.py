from django.shortcuts import render
from .models import Libro
# Create your views here.
def mostrar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'mostrar_libros.html', {'libros':libros})