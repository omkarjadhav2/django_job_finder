from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.show_jobs , name='home'),
    path('register/seeker/', views.register_seeker, name='register_seeker'),
    path('register/employer/', views.register_employer, name='register_employer'),
    path('login', views.user_login , name='login_user'),
    path('accounts/logout/', views.user_logout , name='user_logout'),
    path('jobcard/<slug:slug>', views.job_card , name='job_card'),
    path('apply/<slug:slug>', views.apply_for_job , name='apply_for_job'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.seeker_dashboard, name='seeker_dashboard'),
    path('dashboard/status/<int:id>', views.application_status, name='application_status'),
    
]
