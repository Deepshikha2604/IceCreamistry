from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.profiles,name='profiles'),
    path('', views.user_profile, name='profile'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    
    path('logout/', views.user_logout, name='logout'),
    path('changepassword/', views.user_change_password, 
        name='changepassword'),
    path('changepassword2/', views.user_change_password2, 
        name='changepassword2'),
    path('userdetail/<int:id>', views.user_detail, 
        name='userdetail'),
]
