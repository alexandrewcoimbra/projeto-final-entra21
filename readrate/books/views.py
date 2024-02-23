from django.db import IntegrityError
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.conf import settings
from .models import Livro, Genero, Autor
import requests

# Create your views here.

class BooksListView(ListView):
    model = Livro
    paginate_by = 100
    template_name = "books/index.html"
    ordering = "-id"
    
class BooksSearchView(ListView):
    model = Livro
    paginate_by = 100
    template_name = "books/books_list.html"
    context_object_name = "query"
    ordering = "-id"
    
    def _search_books(self, search_query):
        base_url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": search_query,
            "key": settings.SECRET_KEY,
            "maxResults": 40
        }
        
        try:
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                return response.json().get("items", [])
        except Exception as e:
            print(f"Error searching books: {e}")
        return []
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get("q").strip()
        context["search"] = search.capitalize()
        
        book_queryset = Livro.objects.filter(titulo__icontains=search).order_by("-id")
        context["books"] = book_queryset
        
        return context
    
    def get_queryset(self):
        search = self.request.GET.get("q").strip()
        
        if search:
            api_data = self._search_books(search)
            
            for item in api_data:
                volume_info = item.get("volumeInfo", {})
                title = volume_info.get("title", "N/A")
                
                if Livro.objects.filter(Q(titulo__icontains=title)).exists():
                    continue
                
                pageCount = volume_info.get("pageCount", "N/A")
                authors_list = volume_info.get("authors", ["N/A"])
                genres_list = volume_info.get("categories", ["N/A"])
                
                book = Livro.objects.create(
                    titulo=title,
                    numero_paginas=pageCount,
                )
                
                for author_name in authors_list:
                    existing_authors = Autor.objects.filter(nome__icontains=author_name)
                    
                    if existing_authors.exists():
                        for existing_author in existing_authors:
                            book.autores.add(existing_author)
                    else:
                        new_author = Autor.objects.create(nome=author_name)
                        book.autores.add(new_author)
                        
                for genre_name in genres_list:
                    existing_genres = Genero.objects.filter(nome__icontains=genre_name)
                    
                    if existing_genres.exists():
                        for existing_genre in existing_genres:
                            book.generos.add(existing_genre)
                    else:
                        new_genre = Genero.objects.create(nome=genre_name)
                        book.generos.add(new_genre)
                        
            return Livro.objects.filter(titulo__icontains=search).order_by("-id")
class BooksInformationView(DetailView):
    model = Livro
    template_name = "books/book_info.html"