from django.contrib import admin
from .models import Quest

@admin.register(Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ('title', 'quest_type', 'xp_reward', 'created_at')
    list_filter = ('quest_type',)
