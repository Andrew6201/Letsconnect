
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('navbar/',views.navbar,name='navbar'),
    path('body/',views.body,name='body'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('create_profile/',views.create_profile,name='create_profile'),
    path('specificprofile/<str:pk>/',views.specificprofile,name='specificprofile'),
    path('updateprofile/<str:pk>',views.updateprofile,name='updateprofile'),

    
]
