from rest_framework import serializers
from .models import Quest

class QuestSerializer(serializers.ModelSerializer):
    quest_type_display = serializers.CharField(source='get_quest_type_display', read_only=True)

    class Meta:
        model = Quest
        fields = ['id', 'title', 'description', 'quest_type', 'quest_type_display', 'xp_reward', 'created_at']