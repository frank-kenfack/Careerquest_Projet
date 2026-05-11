from django.shortcuts import render
from rest_framework import viewsets
from .models import Quest
from .serializers import QuestSerializer

class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all().order_by('-created_at') # Du plus récent au plus ancien
    serializer_class = QuestSerializer