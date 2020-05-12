from rest_framework import serializers
from .models import User
from models.serializers import EventSerializer


class UserSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'country', 'address',
                  'date_of_birth', 'events')
