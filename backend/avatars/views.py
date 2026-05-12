from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Avatar
from .serializers import AvatarSerializer

class AvatarViewSet(viewsets.ModelViewSet):
    serializer_class = AvatarSerializer
    permission_classes = [IsAuthenticated] # <--- LE CADENAS EST ICI

    # On modifie la requete pour que l'utilisateur ne voie QUE son propre avatar
    def get_queryset(self):
        return Avatar.objects.filter(user=self.request.user)