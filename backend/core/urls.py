from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from avatars.views import AvatarViewSet
from missions.views import QuestViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'avatars', AvatarViewSet)
router.register(r'missions', QuestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    # Nos nouvelles routes pour l'authentification :
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]