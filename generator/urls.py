from django.urls import path 
from generator import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('password/', views.generator, name='generator'),

]