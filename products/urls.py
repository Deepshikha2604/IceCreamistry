from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('productPage/', views.productPage,name='productPage'),
    path('aboutPage/', views.aboutPage, name='aboutPage'),
    path('ServicePage/', views.ServicePage, name='ServicePage'),
    path('contactPage/', views.contactPage, name='contactPage'),

]
