from django.urls import path
from . import views


urlpatterns = [
    path('', views.f_login, name='f_login'),
    path('notes/', views.f_notes, name='f_notes'),
    path('logout/', views.f_logout, name='f_logout'),
    path('forgot/', views.f_frgtpswd, name='f_frgtpswd'),
    path('dashboard/', views.f_dashboard, name='f_dashboard'),
    path('assingment/', views.f_assingment, name='f_assingment'),
    path('Profile/', views.f_profileUpdate, name='f_profileUpdate'),
    path('assindBatches/', views.f_assindBatches, name='f_assindBatches'),
]