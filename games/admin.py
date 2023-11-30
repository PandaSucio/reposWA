from django.contrib import admin
from .models import Desarrollador
from .models import Género
from .models import Jugador
from .models import Juego

# Register your models here.
admin.site.register(Desarrollador)
admin.site.register(Género)
admin.site.register(Jugador)
admin.site.register(Juego)
