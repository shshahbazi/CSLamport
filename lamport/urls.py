# lamport_app/urls.py
from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
    path('get_hash_iterations/', get_hash_iterations, name='get_hash_iterations'),
    path('set_new_password/<str:username>/', set_new_password, name='set_new_password'),
]
