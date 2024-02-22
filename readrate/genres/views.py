from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from books.models import Livro
from .models import Genero
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    genres = Genero.objects.order_by('nome')
    
    paginator = Paginator(genres, 100)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = { "genres": page_obj }

    return render(request, "genres/index.html", context)

@login_required
def show_gender_books(request, id):
    genre = get_object_or_404(Genero, id=id)
    books = Livro.objects.filter(genre=genre)

    context = {
        'genre': genre,
        'books': books
    }

    return render(request, 'booksbygender.html', context)
