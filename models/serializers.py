from rest_framework import serializers
from .models import Ground, Event, Response


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'name', 'date', 'description', 'creator', 'ground')


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Response
        fields = ("id", "date", "text", "creator", "event", "rating")


class GroundSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ground
        fields = ('id', 'name', 'address', 'coordinates', 'paid', 'ground_type', 'max_players')
