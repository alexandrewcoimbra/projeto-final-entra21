from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("livros", views.index, name='index'),
    path("livros/<slug:slug>/", views.show_book, name="showbook"),
]
