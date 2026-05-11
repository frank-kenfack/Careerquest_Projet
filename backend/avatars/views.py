from django.shortcuts import render
from rest_framework import viewsets
from .models import Avatar
from .serializers import AvatarSerializer

class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer