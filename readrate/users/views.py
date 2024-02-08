from django import forms
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here

def create(request):
    form_action = reverse("users:register")
    
    #POST
    if request.method == "POST":
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "O usuário foi cadastrado com sucesso!")
            
            return redirect("users:index")
        
        context = {
            "form": form,
            "form_action": form_action
        }
        
        return render(request, "users/register.html", context)
    
    # GET
    form = UserForm()
    
    context = {
        "form": form,
        "form_action": form_action
    }
    
    return render(request, "users/register.html", context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:register')  # Redirecione para a URL desejada após o login
            else:
                return HttpResponse("Usuário ou senha inválidos.")
        else:
            return HttpResponse("Formulário inválido.")
    else:
        form = AuthenticationForm()
    return render(request, 'users/index.html', {'form': form})