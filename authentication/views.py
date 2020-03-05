from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_framework import permissions, viewsets

from .models import User
from .serializers import UserSerializer
from .permissions import IsAccountOwner


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class UserViewSet(viewsets.GenericViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'PUT':
            return [permissions.IsAuthenticated(), IsAccountOwner(),]

        if self.request.method == 'POST':
            return [permissions.AllowAny()]

        if self.request.method == 'DELETE':
            return [permissions.IsAuthenticated(), IsAccountOwner(),]

        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]

        return [permissions.IsAuthenticated(), IsAccountOwner(),]

