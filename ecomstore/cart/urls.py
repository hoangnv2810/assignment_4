from django.urls import path
from . import views

from django.urls import path

urlpatterns = [
    path('', views.show_cart, name='show_cart'),
]