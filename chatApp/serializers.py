from enum import unique
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Message, Services, Rating
# 
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    """For Serializing User"""
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    class Meta:
        model = Message
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model=Services
        fields='__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Rating
        fields= '__all__'


class RatingSerializerView(serializers.ModelSerializer):

    client_user = UserSerializer()
    service = ServiceSerializer()
    class Meta:
        model=Rating
        fields= '__all__'
        depth = 1