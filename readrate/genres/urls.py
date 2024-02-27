from django.urls import path
from . import views

app_name = "genres"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:nome>/livros", views.show_gender_books, name="booksbygender")
]
