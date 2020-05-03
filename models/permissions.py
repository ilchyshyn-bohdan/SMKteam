from rest_framework import permissions


class isEventCreator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            return request.user.id == obj.creator
        return False


class isResponseCreator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            return request.user.id == obj.creator
        return False
