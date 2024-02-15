from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    
    books = Livro.objects.order_by('titulo')
    
    paginator = Paginator(books, 100)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = { "books": page_obj }

    return render(request, "books/index.html", context)

def show_book(request, slug):
        book = get_object_or_404(Livro, slug=slug)

        context = {
              'book': book
        }

        return render(request, "books/showbook.html", context)
