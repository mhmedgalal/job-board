from django.urls import path
from . import view_api
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [  
    # API views
  path('register/', view_api.register, name='register'),
  path('me/', view_api.current_user, name='current-user'),
  path('update/', view_api.update_user, name='update_user'),
  path('change-password/', view_api.change_password, name='change_password'),
  path('upload-avatar/', view_api.upload_avatar, name='upload_avatar'),
  path('forgot-password/', view_api.forgot_password, name='forgot-password'),
  path('reset-password/<str:token>/', view_api.reset_password, name='reset-password'),
  # Auth (JWT)
  path('auth/login/', TokenObtainPairView.as_view(), name='jwt-login'),
  path('auth/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
  path('auth/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
  path('auth/logout/', view_api.logout_view, name='jwt-logout'),
]