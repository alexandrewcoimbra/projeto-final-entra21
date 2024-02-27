from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("login/", views.login_view, name="index"),
    path("usuarios/cadastro/", views.create, name="register"),
]
