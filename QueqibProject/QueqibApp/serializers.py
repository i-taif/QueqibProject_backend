from rest_framework import serializers
from .models import City,Post, Profile

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
