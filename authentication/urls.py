from django.urls import path, include
from .views import GoogleLoginView

urlpatterns = [
    path('auth/', include('rest_auth.urls'), name='auth'),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('auth/google/', GoogleLoginView.as_view(), name='google_login'),
]
