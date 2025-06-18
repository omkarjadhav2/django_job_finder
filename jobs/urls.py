from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_job, name='post_job'),
    path('dashboard/', views.employer_dashboard, name='employer_dashboard'),
]
