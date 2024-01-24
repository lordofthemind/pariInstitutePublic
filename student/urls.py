from django.urls import path
from . import views


urlpatterns = [
    path('', views.st_login, name='st_login'),
    path('logout/', views.st_logout, name='st_logout'),
    path('forgot/', views.st_frgtpswd, name='st_frgtpswd'),
    path('register/', views.st_register, name='st_register'),
    path('dashboard/', views.st_dashboard, name='st_dashboard'),
    path('assingment/', views.st_assingment, name='st_assingment'),
    path('Profile/', views.st_profileUpdate, name='st_profileUpdate'),
    path('certificate/', views.st_certificate, name='st_certificate'),
    path('Profilepswd/', views.st_paswrdUpdate, name='st_paswrdUpdate'),
]