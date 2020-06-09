from django.urls import path
from . import views
from .views import AccProfile

urlpatterns = [
    path('register/', views.register , name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('home/profile', AccProfile.as_view(), name='profilepage'),
]