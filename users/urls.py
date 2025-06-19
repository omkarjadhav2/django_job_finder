from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.members , name='home'),
    path('register/employer/', views.register_employer, name='register_employer'),
    path('register/seeker/', views.register_seeker, name='register_seeker'),
    path('login', views.user_login , name='login_user'),
    
]
