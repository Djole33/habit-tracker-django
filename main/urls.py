from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('register', views.register, name="register"),
   path('my-login', views.my_login, name="my-login"),
   path('user-logout', views.user_logout, name="user-logout"),
   path('dashboard', views.dashboard, name="dashboard"),
   path('create-habit', views.create_habit, name='create-habit'),
   path('habit/<int:pk>', views.singular_habit, name='habit'),
   path('update-habit/<int:pk>', views.update_habit, name='update-habit'),
   path('delete-habit/<int:pk>', views.delete_habit, name='delete-habit'),
]
