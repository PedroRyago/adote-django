from django.urls import path
from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]
