from django.contrib import admin
from .models import Avatar

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ('user', 'level', 'current_xp', 'appearance')
    list_filter = ('appearance',)
    search_fields = ('user__username',)
