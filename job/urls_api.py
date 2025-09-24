from django.urls import path
from . import views_api


urlpatterns = [
    path('jobs/', views_api.job_list, name='job_list'),
    path('jobs/<int:pk>/', views_api.job_detail, name='job_detail'),
    path('apply/', views_api.apply, name='apply_job'),
    path('jobs/<int:pk>/applies/', views_api.job_applies, name='job-applies'),
]
