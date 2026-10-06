from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('<int:id>/', views.detalhe, name='detalhe'),
]