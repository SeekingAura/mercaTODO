from django.urls import path
from .views import misProductos

app_name = "sites"

urlpatterns = [
    path('myproducts/', misProductos, name='misProductos'),
]