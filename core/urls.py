from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.register,name = 'vogue-register'),
    path('register/<str:competition_name>/',  views.register, name='vogue-register'),
    path('', views.home,name = 'Vogue-Home'),
]