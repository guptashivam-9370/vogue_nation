from django.urls import path
from . import views

urlpatterns = [
    # path('register/', views.register,name = 'vogue-register'),
    path('register/<str:competition>/',  views.register, name='vogue-register'),
    path('', views.home,name = 'Vogue-Home'),
]