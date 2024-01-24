from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('crsDetail/<uuid:pk>', views.courseDetail, name='courseDetail'),
    path('pricing/', views.pricing, name='pricing'),
]