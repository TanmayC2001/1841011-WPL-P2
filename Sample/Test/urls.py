from .views import home,login
from django.urls import path,include

urlpatterns = [
    path('',home, name = 'home'),
    path('login/', login, name = 'login'),
    
]