from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import Register

urlpatterns = [
     path('register/', Register.as_view(), name='register'),
     path('login/', jwt_views.TokenObtainPairView.as_view(),
         name='obtain_token_pair'),
     path('login/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='refresh_token'),
]
