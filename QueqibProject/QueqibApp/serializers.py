from rest_framework import serializers
from .models import City,Post, Profile , Comment
from django.contrib.auth.models import User

class ViweUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username']

class ViweAllUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'