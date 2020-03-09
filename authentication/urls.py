from django.urls import path, include
from .views import GoogleLoginView, UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls'), name='auth'),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path('auth/google/', GoogleLoginView.as_view(), name='google_login'),
]
