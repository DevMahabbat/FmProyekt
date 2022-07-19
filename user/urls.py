
from django import views

from django.urls import path
from .views import  register
from . import views
urlpatterns = [
   path("register",register ),
   path("login",views.loginF),
   path("logout",views.logOut)
]