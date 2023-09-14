from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "Бот для учета геолокация пользователей"
admin.site.site_title = "Админка бота"


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'external_id',
        'is_active',
        'username',
        'first_name',
        'second_name'
    )
    list_per_page = 50
    list_display_links = list_display


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'latitude',
        'longitude'
    )
    list_per_page = 50
    list_display_links = list_display


class ActionTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

    list_per_page = 50
    list_display_links = list_display

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class UserActionAdmin(admin.ModelAdmin):
    list_display = (
        
        'user',
        'action',
        'time',
        'location'
    )
    list_filter = ('time', 'user', 'action', 'location')
    readonly_fields = ('time',)
    list_per_page = 50
    list_display_links = list_display


admin.site.register(UserAction, UserActionAdmin)
admin.site.register(ActionType, ActionTypeAdmin)
admin.site.register(TelegramUser, UserAdmin)
admin.site.register(Location, LocationAdmin)
