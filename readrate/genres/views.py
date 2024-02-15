from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Genero

def index(request):
    genres = Genero.objects.order_by('nome')
    
    paginator = Paginator(genres, 100)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = { "genres": page_obj }

    return render(request, "genres/index.html", context)

def show_gender_books(request):
    pass
