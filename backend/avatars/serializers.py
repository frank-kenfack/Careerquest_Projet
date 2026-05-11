from rest_framework import serializers
from .models import Avatar
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class AvatarSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True) # Inclut les infos de l'utilisateur
    appearance_display = serializers.CharField(source='get_appearance_display', read_only=True)

    class Meta:
        model = Avatar
        fields = ['id', 'user', 'level', 'current_xp', 'appearance', 'appearance_display']