from django.urls import path
from . import views

app_name = "genres"
urlpatterns = [
    path("", views.index, name="index"),
    path("<nome:nome:>/", views.show_gender_books, name="booksbygender")
]
