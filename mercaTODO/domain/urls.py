from django.urls import path

from .views import Index, Login, Logout

app_name = "domain"

urlpatterns = [
    path('', Index, name='index'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    
]