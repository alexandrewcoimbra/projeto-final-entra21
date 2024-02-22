from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("login", views.login_view, name="index"),
    path("usuarios/cadastro/", views.create, name="register"),
    # path("login/", views.login, name="login"),
    # path("usuarios/<str:username>/", views.update, name="update"),
    # path("usuarios/<int:id>/", views.delete, name="delete")
]
