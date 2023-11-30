from django.urls import path, include
from rest_framework import routers
from games import views

router = routers.DefaultRouter()
router.register(r'juegos', views.JuegoViewSet)
router.register(r'jugadores', views.JugadorViewSet)
router.register(r'genero', views.GéneroViewSet)
router.register(r'desarrolladores', views.DesarrolladorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
