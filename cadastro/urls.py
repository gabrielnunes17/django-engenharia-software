from django.urls import path
from . import views


urlpatterns = [
    path('', views.pagina_login, name='login'),
    path('sobre/', views.pagina_sobre, name='sobre'),
]