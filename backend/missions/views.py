from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Quest
from .serializers import QuestSerializer

class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all().order_by('-created_at')
    serializer_class = QuestSerializer
    permission_classes = [IsAuthenticated] # <--- LE CADENAS EST ICI