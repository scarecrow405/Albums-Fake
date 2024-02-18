from django.contrib import admin

from core.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id_user', 'bio', 'profile_img', 'location')
