from rest_framework import serializers
from .models import Desarrollador
from .models import Género
from .models import Jugador
from .models import Juego


class DesarrolladorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrollador
        # fields = ('fullname', 'nickname')
        fields = '__all__'


class GéneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Género
        # fields = ('fullname', 'nickname')
        fields = '__all__'


class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        # fields = ('fullname', 'nickname')
        fields = '__all__'


class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        # fields = ('fullname', 'nickname')
        fields = '__all__'
