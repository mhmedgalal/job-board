from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('candidate/', views.candidate, name='candidate'),
    path('employer/', views.employer, name='employer'),

]