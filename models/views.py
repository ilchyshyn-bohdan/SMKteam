from rest_framework import permissions, viewsets

from .models import Ground, Event, Response
from .serializers import GroundSerializer, EventSerializer, ResponseSerializer
from .permissions import isEventCreator, isResponseCreator


class GroundViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Ground.objects.all()
    serializer_class = GroundSerializer

    # def get_permissions(self):
    #     if self.request.method == "POST":
    #         return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
    #
    #     if self.request.method == "PUT":
    #         return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
    #
    #     if self.request.method == "DELETE":
    #         return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
    #
    #     if self.request.method == "GET":
    #         return [permissions.AllowAny()]


class EventViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         if self.request.ground.isPrivate:
    #             if self.request.user in self.request.event.users:
    #                 return True
    #             else:
    #                 return [permissions.IsAuthenticated(),
    #                         (permissions.IsAdminUser() or isEventCreator())]
    #         else:
    #             return [permissions.AllowAny()]
    #
    #     if self.request.method == "POST":
    #         return [permissions.IsAuthenticated()]
    #
    #     if self.request.method == "PUT":
    #         return [permissions.IsAuthenticated(),
    #                 (isEventCreator() or permissions.IsAdminUser())]
    #
    #     if self.request.method == "DELETE":
    #         return [permissions.IsAuthenticated(),
    #                 (isEventCreator() or permissions.IsAdminUser())]


class ResponseViewSet(viewsets.ModelViewSet):
    lookup_field = "id"
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

    # def get_permissions(self):
    #     if self.request.method == "GET":
    #         return [permissions.AllowAny()]
    #
    #     if self.request.method == "POST":
    #         return [permissions.IsAuthenticated()]
    #
    #     if self.request.method == "PUT" or "DELETE":
    #         return [isResponseCreator() or permissions.IsAdminUser()]



