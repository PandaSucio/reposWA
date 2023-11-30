from django.forms import ModelForm
from .models import Juego


class CreateJuegos(ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'desarrollador', 'lanzamiento',
                  'genero', 'jugadores', 'portada_url']
