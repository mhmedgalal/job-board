from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # Template views
  path('signup/', views.signup, name='signup'),
  path('profile/', views.profile, name='profile'),
  path('edit_profile/', views.edit_profile, name='edit_profile'),
]