from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.show_jobs , name='home'),
    path('register/seeker/', views.register_seeker, name='register_seeker'),
    path('login', views.user_login , name='login_user'),
    path('accounts/logout/', views.user_logout , name='user_logout'),
    path('jobcard/<slug:slug>', views.job_card , name='job_card'),
    
]
