from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('register', views.register, name="register"),
   path('my-login', views.my_login, name="my-login"),
   path('user-logout', views.user_logout, name="user-logout"),
]
