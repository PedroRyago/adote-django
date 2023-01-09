from django.shortcuts import render
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.http import HttpResponse
from .utils.formFieldsValidate import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
def cadastro(request):

    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if isEmptyField(nome) or isEmptyField(email) or isEmptyField(senha) or isEmptyField(confirmar_senha):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return render(request, 'cadastro.html')

        elif senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não conferem')
            return render(request, 'cadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            return render(request, 'cadastro.html')

        except Exception:
            messages.add_message(request, constants.ERROR, 'Erro ao cadastrar usuário')
            return render(request, 'cadastro.html')

    elif request.method == 'GET':
        return render(request, 'cadastro.html')

def user_login(request):

    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(request, username=nome, password=senha)

        if user is not None:
            login(request, user)
            # messages.add_message(request, constants.SUCCESS, 'Logado com sucesso')
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return render(request, 'login.html')
       

    elif request.method == 'GET':
        return render(request, 'login.html')

def user_logout(request):

    if not request.user.is_authenticated:
        return redirect('/auth/login')

    logout(request)
    messages.add_message(request, constants.SUCCESS, 'Deslogado com sucesso')
    return render(request, 'login.html')