from django.urls import path
from . import views

app_name = "books"
urlpatterns = [
    path("", views.index, name='index'),
    path("<slug:slug>/", views.show_book, name="showbook"),
]
