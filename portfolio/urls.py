from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('habilidades/', views.habilidades, name='habilidades'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyecto/<int:proyecto_id>/', views.proyecto_detalle, name='proyecto_detalle'),
    path('contacto/', views.contacto, name='contacto'),
    path('api/habilidades/', views.api_habilidades, name='api_habilidades'),
]
