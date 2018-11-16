from django.urls import path

from .views import ListProducts
app_name = "products"
urlpatterns = [
    path('', ListProducts, name='listProducts'),
]