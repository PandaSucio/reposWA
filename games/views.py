from django.shortcuts import render
from .models import Desarrollador, Género, Jugador
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Juego, Jugador, Género, Desarrollador
from .forms import CreateJuegos

from rest_framework import viewsets
from .serializers import DesarrolladorSerializer
from .serializers import GéneroSerializer
from .serializers import JugadorSerializer
from .serializers import JuegoSerializer
# Create your views here.
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register users
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('juegos')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'User already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('juegos')


@login_required
def juegos(request):
    juegos = Juego.objects.filter(user=request.user)
    return render(request, 'juegos.html', {'juegos': juegos})


def create_juegos(request):
    if request.method == 'GET':
        return render(request, 'create_juegos.html', {
            'form': CreateJuegos
        })
    else:
        try:
            form = CreateJuegos(request.POST)
            nuevo_juegos = form.save(commit=False)
            nuevo_juegos.user = request.user
            nuevo_juegos.save()
            return redirect('juegos')
        except ValueError:
            return render(request, 'create_juegos.html', {
                'form': CreateJuegos,
                'error': 'Please provide valida data'
            })


@login_required
def componentes(request):
    # Recopila información de las clases que deseas mostrar
    juegos = Juego.objects.all()

    # Puedes personalizar la forma en que combinas la información según tus necesidades
    context = {
        'juegos': juegos,
    }

    return render(request, 'componentes.html', context)


# Api import


class DesarrolladorViewSet(viewsets.ModelViewSet):
    queryset = Desarrollador.objects.all()
    serializer_class = DesarrolladorSerializer


class GéneroViewSet(viewsets.ModelViewSet):
    queryset = Género.objects.all()
    serializer_class = GéneroSerializer


class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer


class JuegoViewSet(viewsets.ModelViewSet):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
