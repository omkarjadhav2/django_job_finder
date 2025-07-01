from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_job, name='post_job'),
    path('dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('dashboard/update/<slug:slug>/', views.update_post, name='update_job'),
    path('dashboard/delete/<slug:slug>/', views.delete_post, name='delete_job'),
    path('applications/<slug:slug>', views.view_applications, name='view_applications'),
]
