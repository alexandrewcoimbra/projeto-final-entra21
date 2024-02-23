from django.urls import path
from .views import BooksSearchView, BooksListView, BooksInformationView

app_name = "books"
urlpatterns = [
    path("", BooksListView.as_view(), name="index"),
    path("search", BooksSearchView.as_view(), name="search"),
    path("books/<slug:slug>/", BooksInformationView.as_view(), name="info"),
]
