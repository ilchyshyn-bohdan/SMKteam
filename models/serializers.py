from rest_framework import serializers
from .models import Ground, Event, Response
from authentication.models import User


class EventSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'description', 'creator', 'users', 'ground')


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Response
        fields = ("id", "date", "text", "creator", "event", "rating")


class UserResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Response
        fields = ("id", "date", "text", "creator", "target", "rating")


class GroundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ground
        fields = ('id', 'name', 'address', 'coordinates', 'paid', 'ground_type', 'max_players')
