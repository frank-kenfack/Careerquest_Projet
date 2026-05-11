from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from avatars.views import AvatarViewSet
from missions.views import QuestViewSet

# Le router genere automatiquement les URLs pour nos ViewSets
router = DefaultRouter()
router.register(r'avatars', AvatarViewSet)
router.register(r'missions', QuestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Toutes nos donnees seront sous /api/...
]